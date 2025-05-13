import copy
import importlib.util
import json
import os
import sys

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
    temp = os.environ.get("FLET_APP_STORAGE_TEMP")
    permanent = os.environ.get("FLET_APP_STORAGE_DATA")

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

    for key, value in data.items():
        # Loops through the configuration dictionary
        # content for building each
        # Json can be loaded using json.load but python
        # files need a proper module import

        # Entity file is the one containing structure, type,
        # and other important type related info
        entity_file = value.get("entity_file")
        if ".json" in entity_file:
            try:
                loc = temp + "/" + map_name + "/"
                with open(loc + entity_file[:-5]) as file:
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

            fp = temp + "/" + map_name + "/" + entity_file
            ef = entity_file[:-2]
            spec = importlib.util.spec_from_file_location(ef, fp)
            try:
                module1 = importlib.util.module_from_spec(spec)
                sys.modules[entity_file] = module1
                spec.loader.exec_module(module1)
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

        if value.get("res_file"):
            # Res or say Resource file contains the cards to be registered
            # If res file isn't present, this means that the cards are all
            # common and can be registered using the num var in
            # configuration file
            res_file = value.get("res_file")
            if ".json" in res_file:
                try:
                    loc = temp + "/" + map_name + "/"
                    with open(loc + res_file[:-5]) as file:
                        data_3 = json.load(file)
                except Exception:
                    raise GameFunctioningException(
                        f"""No file found at
                        {temp}/{map_name}/{res_file}"""
                    )
            elif ".py" in value.get("res_file"):

                fp = temp + "/" + map_name + "/" + res_file
                rf = res_file[:-2]
                spec = importlib.util.spec_from_file_location(rf, fp)
                try:
                    module2 = importlib.util.module_from_spec(spec)
                    sys.modules[res_file] = module2
                    spec.loader.exec_module(module2)
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
            for card, card_value in data_3.items():
                if card_value.get("type") in value.get("types"):
                    structure = copy.deepcopy(
                        data_2.get(card_value.get("type")).get("structure")
                    )
                    if not structure:
                        raise GameFunctioningException(
                            f"""Structure details
                        empty for asset {card} of type {card_value.get('type')}
                        in file temp/
                        {map_name}/{value.get('entity_file')}
                        """
                        )
                    a_temp_struc = structure["others"]
                    for i in structure.get("others"):
                        a_temp = a_temp_struc[structure.get("others").index(i)]
                        if type(i.get("reqs")) == str:
                            a_temp["reqs"] = eval(i.get("reqs"))
                    try:
                        anothtemp = data_2.get(card_value.get("type"))
                        folder = str(f"{permanent}/{anothtemp.get("assets")}")
                        os.makedirs(folder, exist_ok=True)
                        create_asset(structure).save(
                            f"{permanent}/{anothtemp.get('assets')}/{card}.png"
                        )
                    except Exception:
                        raise GameFunctioningException("Asset Creation Fail !")

        # This is for building same cards acc to the num var in the config file
        else:
            for k in value.get("types"):
                for j in range(value.get("num")):
                    try:
                        folder = f"{permanent}/{data_2.get(k).get("assets")}"
                        os.makedirs(folder, exist_ok=True)
                        a = data_2.get(k).get("assets")
                        b = create_asset(structure)
                        b.save(f"{permanent}/{a}/{k}_{j}.png")
                    except Exception:
                        msg = "Asset Creation Failed !"
                        raise GameFunctioningException(msg)
