import os

import flet as ft

from download_maps import download_map


def main(page: ft.Page):
    os.environ["DRIVE_MAP_ROOT_LINK"] = "Bankory"
    async def download_the_map(e):
        down = ft.Text("Downloading")
        page.add(
            down
        )
        page.update()
        await download_map('map_01')
    page.add(
        ft.FilledButton("Download Map",on_click=download_the_map)
    )
    page.update()


ft.app(main)
