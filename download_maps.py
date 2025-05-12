import shutil
import os
from download_files import download
import json
from exceptions import GameFunctioningException
from asset_builder import build

def download_map(map_name):
    temp = os.environ.get('TEMPORARY_STORAGE_LOCATION')
    permanent = os.environ.get('PERMANENT_STORAGE_LOCATION')
    
    map_root = os.environ.get('DRIVE_MAP_ROOT_LINK')
    if not map_root:
        raise GameFunctioningException("Root link for map retrieval from google drive missing !")
    
    download(map_root + map_name,temp)

    with open(f"{temp}/{map_name}/{map_name}.json") as file:
        data = json.load(file)

    for i in data:
        if type(data.get(i))==dict:
            if data.get(i).get('permanent'):
                if type(data.get(i).get('file_name'))==list:
                    if data.get(i).get('save_folder'):
                        save_folder = data.get(i).get('save_folder')
                    else:
                        save_folder = "."
                    for g in data.get(i).get('file_name'):
                        download('Bankory/' + data.get('root') + data.get(i).get('retrieve_folder') + g,permanent + save_folder)
                elif type(data.get(i).get('file_name'))==str:
                    download('Bankory/' + data.get('root') + data.get(i).get('retrieve_folder') + data.get(i).get('file_name'),permanent + save_folder)
                else:
                    raise GameFunctioningException(f"Unintended file configuration found in temp/{map_name}/{map_name}.json")
        elif type(data.get(i))==str:
            os.environ[i] = data.get(i)
        else:
            raise GameFunctioningException(f"Unintended file configuration found in temp/{map_name}/{map_name}.json")
        
    assets = data.get('asset_configuration_file').get('file_name')
    if type(assets)==list:
        for i in assets:
            build(i,map_name)
    elif type(assets)==str:
        build(assets,map_name)
    else:
        raise GameFunctioningException(f"Unintended file configuration found in temp/{map_name}/{map_name}.json")

download_map("map_01")