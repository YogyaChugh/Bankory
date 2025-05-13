import json
import os

from asset_builder import build
from download_files import download
from exceptions import GameFunctioningException


async def download_map(map_name):
    # Handles everything from downloading
    # all files of a map in temp folder of flet,
    # saving permanent files and building the assets
    temp = os.environ.get("FLET_APP_STORAGE_TEMP")
    permanent = os.environ.get("FLET_APP_STORAGE_DATA")

    map_root = os.environ.get("DRIVE_MAP_ROOT_LINK")
    if not map_root:
        raise GameFunctioningException(
            """
            Root link for map retrieval from Google Drive missing!
        """
        )

    try:
        # Downloads the whole folder of the map in temp folder
        print("Downloading.......")
        download(map_root + "/maps/" + map_name, temp)
        print("Downloaded all files !")
    except Exception:
        raise GameFunctioningException(
            f"""
            Root download for map {map_name} failed !
            """
        )

    map_json_path = os.path.join(temp, map_name, f"{map_name}.json")
    with open(map_json_path) as file:
        data = json.load(file)

    print(data)

    for key, value in data.items():
        print(value)
        print(type(value))
        if isinstance(value, dict):
            if value.get("permanent"):
                save_folder = value.get("save_folder", ".")
                file_name = value.get("file_name")

                if isinstance(file_name, list):
                    for g in file_name:
                        try:
                            download(
                                (
                                    "Bankory/"
                                    + data.get("root", "")
                                    + value.get("retrieve_folder", "")
                                    + g
                                ),
                                os.path.join(permanent, save_folder),
                            )
                        except Exception:
                            raise GameFunctioningException(
                                f"""
                                Root download for map
                                {map_name}'s file {g} failed
                            """
                            )
                elif isinstance(file_name, str):
                    try:
                        download(
                            (
                                "Bankory/"
                                + data.get("root", "")
                                + value.get("retrieve_folder", "")
                                + file_name
                            ),
                            os.path.join(permanent, save_folder),
                        )
                    except Exception:
                        raise GameFunctioningException(
                            f"""
                            Root download for map
                            {map_name}'s file {file_name} failed
                        """
                        )
                else:
                    raise GameFunctioningException(
                        f"""
                        Unintended file configuration found in {map_json_path}
                    """
                    )
        elif isinstance(value, str):
            os.environ[key] = value
        else:
            raise GameFunctioningException(
                f"""
                Unintended file configuration found in {map_json_path}
            """
            )

    # Build assets
    assets = data.get("asset_configuration_file", {}).get("file_name")
    if isinstance(assets, list):
        for i in assets:
            build(i, map_name)
    elif isinstance(assets, str):
        build(assets, map_name)
    else:
        raise GameFunctioningException(
            f"""
            Unintended file configuration found in {map_json_path}
        """
        )
    return
