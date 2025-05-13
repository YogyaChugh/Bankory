data = {
    "BOARD": {
        "assets": "maps/map_01/assets/board/",
        "structure": {
            "main": {
                "type": "color",
                "color": (230, 220, 200),
                "dimensions": (250, 400),
                "border_width": 4,
                "border_color": (90, 60, 40),
                "self_distance": True,
            },
            "others": [
                {
                    "type": "rectangle",
                    "reqs": """(((0, 0), (250, 80)),
                            (255,255,0), (90, 60, 40), 4)"""
                },
                {
                    "type": "text",
                    "reqs": """[['center', 130], "Hello ji", (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 30)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True
                },
                {
                    "type": "text",
                    "reqs": """[['center', 200], 'PRICE', (90, 60, 40),
                             ImageFont.truetype('DejaVuSans.ttf', 25)]""",
                    "spacing": 50,
                    "margin": (20, 20, 20, 20),
                    "shorten": True
                },
                {
                    "type": "text",
                    "reqs": """[['center', 210], '$' +
                            100,
                            (55, 40, 30),
                            ImageFont.truetype('DejaVuSans.ttf', 30)]""",
                    "spacing": 50,
                    "margin": (20, 20, 20, 20),
                    "shorten": True
                }
            ]
        }
    }
}
