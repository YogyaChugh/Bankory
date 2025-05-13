from PIL import Image

data = {
    "PROPERTY": {
        "ownable": True,
        "rentable": True,
        "house": True,
        "mortgage": True,
        "board": True,
        "actions": True,
        "assets": "maps/map_01/assets/cards/property_card",
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
                            card_value.get('color'), (90, 60, 40), 4)"""
                },
                {
                    "type": "text",
                    "reqs": """[['center', 130], card, (90, 60, 40),
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
                            str(card_value.get('price')),
                            (55, 40, 30),
                            ImageFont.truetype('DejaVuSans.ttf', 30)]""",
                    "spacing": 50,
                    "margin": (20, 20, 20, 20),
                    "shorten": True
                }
            ]
        }
    },
    "STATION": {
        "ownable": True,
        "rentable": True,
        "house": False,
        "mortgage": True,
        "board": True,
        "actions": True,
        "assets": "maps/map_01/assets/cards/station_card",
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
                    "type": "text",
                    "reqs": """[['center', 50], card, (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 28)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True
                },
                {
                    "type": "image",
                    "location": "map_01/assets/rail.png",
                    "position": (3, 150),
                    "scale": ((255, 164), Image.Resampling.LANCZOS)
                },
                {
                    "type": "text",
                    "reqs": """[['center', 320],'$' +
                            str(card_value.get('price')),
                            (55, 40, 30),
                            ImageFont.truetype('DejaVuSans.ttf', 28)]""",
                    "spacing": 50,
                    "margin": (20, 20, 20, 20),
                    "shorten": True
                }
            ]
        }
    },
    "WATER WORKS": {
        "ownable": True,
        "rentable": True,
        "house": False,
        "mortgage": True,
        "board": True,
        "actions": True,
        "assets": "maps/map_01/assets/cards/water_works_card",
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
                    "type": "text",
                    "reqs": """[['center', 50], card, (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 30)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True
                },
                {
                    "type": "image",
                    "location": "map_01/assets/water_tap.png",
                    "position": ('center', 130),
                    "scale": ((255, 164), Image.Resampling.LANCZOS)
                },
                {
                    "type": "text",
                    "reqs": """[['center', 320], '$' +
                            str(card_value.get('price')),
                            (55, 40, 30),
                            ImageFont.truetype('DejaVuSans.ttf', 30)]""",
                    "spacing": 50,
                    "margin": (20, 20, 20, 20),
                    "shorten": True
                }
            ]
        }
    },
    "ELECTRIC COMPANY": {
        "ownable": True,
        "rentable": True,
        "house": False,
        "mortgage": True,
        "board": True,
        "actions": True,
        "assets": "maps/map_01/assets/cards/electric_company_card",
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
                    "type": "text",
                    "reqs": """[['center', 50], card, (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 28)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True
                },
                {
                    "type": "image",
                    "location": "map_01/assets/bulb.png",
                    "position": ('center', 150),
                    "scale": ((139, 157), Image.Resampling.LANCZOS)
                },
                {
                    "type": "text",
                    "reqs": """[['center', 320], '$' +
                            str(card_value.get('price')),
                            (55, 40, 30),
                            ImageFont.truetype('DejaVuSans.ttf', 28)]""",
                    "spacing": 50,
                    "margin": (20, 20, 20, 20),
                    "shorten": True
                }
            ]
        }
    },
    "FREE PARKING": {
        "ownable": False,
        "rentable": False,
        "house": False,
        "mortgage": False,
        "board": True,
        "actions": True,
        "assets": "maps/map_01/assets/cards/bus_stop_card",
        "structure": {
            "main": {
                "type": "color",
                "color": (230, 220, 200),
                "dimensions": (400, 400),
                "border_width": 4,
                "border_color": (90, 60, 40)
            },
            "others": [
                {
                    "type": "image",
                    "location": "map_01/assets/bus.png",
                    "position": ('center', 'center'),
                    "scale": ((314, 292), Image.Resampling.LANCZOS),
                    "rotate": 45
                },
                {
                    "type": "text",
                    "reqs": """[['center', 20], 'FREE', (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 50)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True,
                    "rotate": 45
                },
                {
                    "type": "text",
                    "reqs": """[['center', 300], 'PARKING', (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 50)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True,
                    "rotate": 45
                }
            ]
        }
    },
    "CHANCE": {
        "ownable": False,
        "rentable": False,
        "house": False,
        "mortgage": False,
        "board": True,
        "actions": True,
        "assets": "maps/map_01/assets/cards/chance_card",
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
                    "type": "text",
                    "reqs": """[['center', 50], card, (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 28)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True
                },
                {
                    "type": "image",
                    "location": "map_01/assets/question_mark.png",
                    "position": ('center', 150),
                    "scale": ((125, 165), Image.Resampling.LANCZOS)
                }
            ]
        }
    },
    "COMMUNITY CHEST": {
        "ownable": False,
        "rentable": False,
        "house": False,
        "mortgage": False,
        "board": True,
        "actions": True,
        "assets": "maps/map_01/assets/cards/community_card",
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
                    "type": "text",
                    "reqs": """[['center', 50], card, (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 28)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True
                },
                {
                    "type": "image",
                    "location": "map_01/assets/chest.png",
                    "position": ('center', 180),
                    "scale": ((154, 135), Image.Resampling.LANCZOS)
                }
            ]
        }
    },
    "JAIL VISIT": {
        "ownable": False,
        "rentable": False,
        "house": False,
        "mortgage": False,
        "board": True,
        "actions": False,
        "assets": "maps/map_01/assets/cards/jail_visit_card",
        "structure": {
            "main": {
                "type": "color",
                "color": (230, 220, 200),
                "dimensions": (400, 400),
                "border_width": 4,
                "border_color": (90, 60, 40)
            },
            "others": [
                {
                    "type": "image",
                    "location": "map_01/assets/man_in_jail.png",
                    "position": ('center', 'center'),
                    "scale": ((314, 292), Image.Resampling.LANCZOS),
                    "rotate": 45
                },
                {
                    "type": "text",
                    "reqs": """[['center', 30], 'JAIL TIME', (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 35)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True,
                    "rotate": 43
                },
                {
                    "type": "text",
                    "reqs": """[['center', 310], 'CRY NOW !', (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 35)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True,
                    "rotate": 43
                }
            ]
        }
    },
    "GO TO JAIL": {
        "ownable": False,
        "rentable": False,
        "house": False,
        "mortgage": False,
        "board": True,
        "actions": True,
        "assets": "maps/map_01/assets/cards/jail_card",
        "structure": {
            "main": {
                "type": "color",
                "color": (230, 220, 200),
                "dimensions": (400, 400),
                "border_width": 4,
                "border_color": (90, 60, 40)
            },
            "others": [
                {
                    "type": "image",
                    "location": "map_01/assets/police.png",
                    "position": ('center', 'center'),
                    "scale": ((314, 292), Image.Resampling.LANCZOS),
                    "rotate": 45
                },
                {
                    "type": "text",
                    "reqs": """[['center', 20], 'GO TO', (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 50)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True,
                    "rotate": 45
                },
                {
                    "type": "text",
                    "reqs": """[['center', 320], 'JAIL', (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 50)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True,
                    "rotate": 45
                }
            ]
        }
    },
    "INCOME TAX": {
        "ownable": False,
        "rentable": False,
        "house": False,
        "mortgage": False,
        "board": True,
        "actions": True,
        "assets": "maps/map_01/assets/cards/income_tax_card",
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
                    "type": "text",
                    "reqs": """[['center', 50], card, (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 28)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10),
                    "shorten": True
                },
                {
                    "type": "image",
                    "location": "map_01/assets/money_bag.png",
                    "position": ('center', 143),
                    "scale": ((175, 200), Image.Resampling.LANCZOS)
                }
            ]
        }
    }
}
