import json
import os
import importlib
from assets_creator import create_asset
import copy
from exceptions import GameFunctioningException

def build(file_name,map_name):

    temp = os.environ.get('TEMPORARY_STORAGE_LOCATION')
    permanent = os.environ.get('PERMANENT_STORAGE_LOCATION')

    if not temp or not permanent:
        raise GameFunctioningException("Temporary/Permanent storage locations are empty !!")

    try:
        with open(temp + "/" + map_name + "/" + file_name) as file:
            data = json.load(file)
    except Exception as e:
        raise GameFunctioningException(f"No file found at {temp}/{map_name}/{file_name}")
    
    if not data:
        raise GameFunctioningException(f"File at {temp}/{map_name}/{file_name} is empty !")
    
    data_2 = {}
    data_3 = {}
    
    for i in data:
        if ".json" in data.get(i).get('entity_file'):
            try:
                with open(temp + "/" + map_name + "/" + data.get(i).get('entity_file')) as file:
                    data_2 = json.load(file)
            except Exception as e:
                raise GameFunctioningException(f"No file found at {temp}/{map_name}/{data.get(i).get('entity_file')}")
            
            if not data_2:
                raise GameFunctioningException(f"File at {temp}/{map_name}/{data.get(i).get('entity_file')} is empty !")
        elif ".py" in data.get(i).get('entity_file'):
            try:
                module1 = importlib.import_module(temp + "." + map_name + "." + data.get(i).get('entity_file'))
            except Exception as e:
                raise GameFunctioningException(f"No file found at {temp}/{map_name}/{data.get(i).get('entity_file')}")
            if not module1:
                raise GameFunctioningException(f"File at {temp}/{map_name}/{data.get(i).get('entity_file')} is empty !")
            data_2 = module1.data
        
        if data.get(i).get('res_file'):
            if '.json' in data.get(i).get('res_file'):
                try:
                    with open(temp + "/" + map_name + "/" + data.get(i).get('res_file')) as file:
                        data_3 = json.load(file)
                except Exception as e:
                    raise GameFunctioningException(f"No file found at {temp}/{map_name}/{data.get(i).get('res_file')}")
            elif ".py" in data.get(i).get('res_file'):
                try:
                    module2 = importlib.import_module(temp + "." + map_name + "." + data.get(i).get('res_file'))
                except Exception as e:
                    raise GameFunctioningException(f"No file found at {temp}/{map_name}/{data.get(i).get('res_file')}")
                if not module2:
                    raise GameFunctioningException(f"File at {temp}/{map_name}/{data.get(i).get('res_file')} is empty !")
                data_3 = module2.data

        if data_3:
            for j in data_3:
                if data_3.get(j).get('type') in data.get(i).get('types'):
                    structure = copy.deepcopy(data_2.get(data_3.get(j).get('type')).get('structure'))
                    if not structure:
                        raise GameFunctioningException(f"Structure details empty for asset {j} of type {data_3.get(j).get('type')} in file temp/{map_name}/{data.get(i).get('entity_file')}")
                    for i in structure.get('others'):
                        if type(i.get('reqs'))== str:
                            structure['others'][structure.get('others').index(i)]['reqs'] = eval(i.get('reqs'))
                    try:
                        create_asset(structure).save(f'{permanent}/{data_2.get(data_3.get(j).get('type')).get("assets")}/{j}.png')
                    except Exception as e:
                        raise GameFunctioningException(f'Asset Creation Failed ! Error log: {e.message}')