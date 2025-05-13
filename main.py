import asyncio
import os

import flet as ft

from download_maps import download_map


async def main(page: ft.Page):
    os.environ["DRIVE_MAP_ROOT_LINK"] = "Bankory"

    async def download_the_map(e):
        dd = ft.Text("Downloading Assets", size=30)
        ddd = ft.Lottie(
            src="https://lottie.host/112cc440-9996-"
            "4940-88e0-760478f1df16/1PmwcuuXBz.json",
            animate=True,
        )
        page.add(dd, ddd)
        page.update()
        await asyncio.sleep(1)
        await download_map("map_01")
        dd.value = "Assets Downloaded Successfully !!"
        ddd.src = (
            "https://lottie.host/971d8194-8ff6-"
            "4977-b0b0-b130fc8b65c9/noCrIB4ycY.json"
        )
        page.update()

    page.add(ft.FilledButton("Download Map", on_click=download_the_map))
    page.update()


ft.app(main)
