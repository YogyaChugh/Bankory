import os

from asset_builder import build

os.environ["FLET_APP_STORAGE_TEMP"] = "storage/temp"
os.environ["FLET_APP_STORAGE_DATA"] = "storage/data"

build("configuration.json", "map_01")
