import os

import flet as ft

from download_maps import download_map


def main(page: ft.Page):
    os.environ["DRIVE_MAP_ROOT_LINK"] = "Bankory"
    download_map("map_01")
    page.update()


ft.app(main)
