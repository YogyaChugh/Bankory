import copy
import importlib
import json
import os

from PIL import ImageFont

from assets_creator import create_asset
from exceptions import GameFunctioningException

# Just ignore this !
random_guy = ImageFont.truetype("arial.ttf", 10)


# Just to explain, the configuration file has got a types
# list which gives the types linked together under 1 file
# entity_file is the one containing information
# about those each types in the list
# res_file is optional and contains the different
# cards/assets of each type
# Finally, the num is optional and present if res_file isn't
# and defines the number of assets to build


def build(file_name, map_name):
    """
    Builds the resources based on the configuration
    file provided and the map name.
    """

    # These are provided by flet library for use when packaged !
    temp = os.environ.get("TEMPORARY_STORAGE_LOCATION")
    permanent = os.environ.get("PERMANENT_STORAGE_LOCATION")

    if not temp or not permanent:
        raise GameFunctioningException(
            """Temporary/Permanent
                            storage locations are empty !!"""
        )

    try:
        with open(temp + "/" + map_name + "/" + file_name) as file:
            data = json.load(file)
    except Exception:
        raise GameFunctioningException(
            f"""No file found at
            {temp}/{map_name}/{file_name}"""
        )

    if not data:
        raise GameFunctioningException(
            f"""File at
            {temp}/{map_name}/{file_name} is empty !"""
        )

    data_2 = {}
    data_3 = {}

    for i in data:
        # Loops through the configuration dictionary
        # content for building each
        # Json can be loaded using json.load but python
        # files need a proper module import

        # Entity file is the one containing structure, type,
        # and other important type related info
        entity_file = data.get(i).get("entity_file")
        if ".json" in entity_file:
            try:
                with open(temp + "/" + map_name + "/" + entity_file) as file:
                    data_2 = json.load(file)
                    # Contains the data of all types
            except Exception:
                raise GameFunctioningException(
                    f"""No file found at
                    {temp}/{map_name}/{entity_file}"""
                )

            if not data_2:
                raise GameFunctioningException(
                    f"""File at
                {temp}/{map_name}/{entity_file}
                is empty !"""
                )
        elif ".py" in entity_file:
            try:
                module1 = importlib.import_module(
                    temp + "." + map_name + "." + entity_file
                )
            except Exception:
                raise GameFunctioningException(
                    f"""No file found at
                {temp}/{map_name}/{entity_file}"""
                )
            if not module1:
                raise GameFunctioningException(
                    f"""File at
                {temp}/{map_name}/{entity_file}
                is empty !"""
                )
            data_2 = module1.data
            # Every python data file has got a data variable

        if data.get(i).get("res_file"):
            # Res or say Resource file contains the cards to be registered
            # If res file isn't present, this means that the cards are all
            # common and can be registered using the num var in
            # configuration file
            res_file = data.get(i).get("res_file")
            if ".json" in res_file:
                try:
                    with open(temp + "/" + map_name + "/" + res_file) as file:
                        data_3 = json.load(file)
                except Exception:
                    raise GameFunctioningException(
                        f"""No file found at
                        {temp}/{map_name}/{res_file}"""
                    )
            elif ".py" in data.get(i).get("res_file"):
                try:
                    module2 = importlib.import_module(
                        temp + "." + map_name + "." + res_file
                    )
                except Exception:
                    raise GameFunctioningException(
                        f"""No file found at
                        {temp}/{map_name}/{res_file}"""
                    )
                if not module2:
                    raise GameFunctioningException(
                        f"""File at
                        {temp}/{map_name}/
                        {res_file} is empty !"""
                    )
                data_3 = module2.data

        # This is for building all cards in the resource file
        if data_3:
            for j in data_3:
                if data_3.get(j).get("type") in data.get(i).get("types"):
                    structure = copy.deepcopy(
                        data_2.get(data_3.get(j).get("type")).get("structure")
                    )
                    if not structure:
                        raise GameFunctioningException(
                            f"""Structure details
                        empty for asset {j} of type {data_3.get(j).get('type')}
                        in file temp/
                        {map_name}/{data.get(i).get('entity_file')}
                        """
                        )
                    a_temp = structure["others"]
                    a_temp = a_temp[structure.get("others").index(i)]
                    for i in structure.get("others"):
                        if type(i.get("reqs")) == str:
                            a_temp["reqs"] = eval(i.get("reqs"))
                    try:
                        create_asset(structure).save(
                            f"""{permanent}/
                        {data_2.get(data_3.get(j).get('type')).get("assets")}
                        /{j}.png"""
                        )
                    except Exception as e:
                        raise GameFunctioningException(
                            f"""Asset
                            Creation Failed ! Error log: {e.message}"""
                        )

        # This is for building same cards acc to the num var in the config file
        else:
            for k in data.get(i).get("types"):
                for j in range(data.get(i).get("num")):
                    try:
                        create_asset(structure).save(
                            f"""{permanent}/
                            {data_2.get(k).get("assets")}/{k}_{j}.png"""
                        )
                    except Exception as e:
                        raise GameFunctioningException(
                            f"""Asset Creation
                            Failed ! Error log: {e.message}"""
                        )
