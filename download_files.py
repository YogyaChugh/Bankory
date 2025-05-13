"""
I have no idea about how this works !
It's just taken from google and AI !
It's download() function downloads the requested
file/folder at the destination location provided !

Rest all code/files (except 3 functions) written by @YogyaChugh :)

- I love self-written code ! That's why !
"""

import io
import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from exceptions import GameFunctioningException

SCOPES = ["https://www.googleapis.com/auth/drive"]


def get_gdrive_service():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "auth/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("drive", "v3", credentials=creds)


def search(service, query):
    result = []
    page_token = None
    while True:
        response = (
            service.files()
            .list(
                q=query,
                spaces="drive",
                fields="nextPageToken, files(id, name, mimeType)",
                pageToken=page_token,
            )
            .execute()
        )
        for file in response.get("files", []):
            result.append((file["id"], file["name"], file["mimeType"]))
        page_token = response.get("nextPageToken", None)
        if not page_token:
            break
    return result


def download_file(service, file_id, filename, destination):
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(os.path.join(destination, filename), "wb")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        if status:
            print(f"  Downloaded {int(status.progress() * 100)}%.")


def download_folder(service, folder_id, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    # list files in folder
    query = f"'{folder_id}' in parents and trashed=false"
    items = search(service, query)
    for file_id, name, mime in items:
        if mime == "application/vnd.google-apps.folder":
            # It's a subfolder — recursive call
            download_folder(service, file_id, os.path.join(destination, name))
        else:
            # It's a file — download
            download_file(service, file_id, name, destination)


def make_shareable(service, file_id):
    try:
        service.permissions().create(
            body={"role": "reader", "type": "anyone"}, fileId=file_id
        ).execute()
    except Exception:
        raise GameFunctioningException(
            f"""Couldn't set
        permissions of file ! {file_id}"""
        )


def find_path(service, path):
    parts = path.strip("/").split("/")
    parent = "root"

    for i, name in enumerate(parts):
        is_last = i == len(parts) - 1
        query = f"'{parent}' in parents and name='{name}' and trashed=false"
        results = search(service, query)
        if not results:
            return None, None, None
        # Prefer folders if not at the last part
        if not is_last:
            for fid, fname, mime in results:
                if mime == "application/vnd.google-apps.folder":
                    parent = fid
                    break
            else:
                return None, None, None
        else:
            # Accept either file or folder
            return results[0]  # (id, name, mime)
    return None, None, None


def download(remote_path, local_destination):
    service = get_gdrive_service()
    file_id, file_name, mime = find_path(service, remote_path)

    if not file_id:
        raise GameFunctioningException(
            f"""Folder/File
        not found at {remote_path}"""
        )

    make_shareable(service, file_id)

    # Ensure the destination directory exists
    os.makedirs(local_destination, exist_ok=True)

    if mime == "application/vnd.google-apps.folder":
        final_destination = os.path.join(local_destination, file_name)
        download_folder(service, file_id, final_destination)
    else:
        download_file(service, file_id, file_name, local_destination)
