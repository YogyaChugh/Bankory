from PIL import Image

data = {
    "BOARD": {
        "assets": "maps/map_01/assets/board/",
        "structure": {
            "main": {
                "type": "color",
                "color": (230, 220, 200),
                "dimensions": (626,626),
                "border_width": 8,
                "border_color": (90, 60, 40),
                "self_distance": True,
            },
            "others": [
                {
                    "type": "text",
                    "reqs": """[['center', 'center'], 'BANKORY', (90, 60, 40),
                            ImageFont.truetype('DejaVuSans-Bold.ttf', 60)]""",
                    "spacing": 50,
                    "margin": (10, 10, 10, 10)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/start_card/START.png",
                    "position": (538,538),
                    "scale": ((80,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Old Kent Road.png",
                    "position": (488,538),
                    "scale": ((50,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/community_card/COMMUNITY CHEST.png",
                    "position": (438,538),
                    "scale": ((50,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Whitechapel Road.png",
                    "position": (388,538),
                    "scale": ((50,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/income_tax_card/INCOME TAX.png",
                    "position": (338,538),
                    "scale": ((50,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/station_card/Kings Cross Station.png",
                    "position": (288,538),
                    "scale": ((50,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/The Angel, Islington.png",
                    "position": (238,538),
                    "scale": ((50,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/chance_card/CHANCE.png",
                    "position": (188,538),
                    "scale": ((50,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Euston Road.png",
                    "position": (138,538),
                    "scale": ((50,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Pentonville Road.png",
                    "position": (88,538),
                    "scale": ((50,80), Image.Resampling.LANCZOS)
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/jail_visit_card/JAIL VISIT.png",
                    "position": (8,538),
                    "scale": ((80,80), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Pall Mall.png",
                    "position": (8,488),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/electric_company_card/Electric Company.png",
                    "position": (8,438),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Whitehall.png",
                    "position": (8,388),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Northumberland Avenue.png",
                    "position": (8,338),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/station_card/Marylebone Station.png",
                    "position": (8,288),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Bow Street.png",
                    "position": (8,238),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/community_card/COMMUNITY CHEST.png",
                    "position": (8,188),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Marlborough Street.png",
                    "position": (8,138),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Vine Street.png",
                    "position": (8,88),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": -90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/free_parking_card/FREE PARKING.png",
                    "position": (8,8),
                    "scale": ((80,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Strand.png",
                    "position": (88,8),
                    "scale": ((50,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/chance_card/CHANCE.png",
                    "position": (138,8),
                    "scale": ((50,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Fleet Street.png",
                    "position": (188,8),
                    "scale": ((50,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Trafalgar Square.png",
                    "position": (238,8),
                    "scale": ((50,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/station_card/Fenchurch St Station.png",
                    "position": (288,8),
                    "scale": ((50,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Leicester Square.png",
                    "position": (338,8),
                    "scale": ((50,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Coventry Street.png",
                    "position": (388,8),
                    "scale": ((50,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/water_works_card/Water Works.png",
                    "position": (438,8),
                    "scale": ((50,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Piccadilly.png",
                    "position": (488,8),
                    "scale": ((50,80), Image.Resampling.LANCZOS),
                    "rotate": 180
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/jail_card/GO TO JAIL.png",
                    "position": (538,8),
                    "scale": ((80,80), Image.Resampling.LANCZOS),
                    "rotate": 90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Regent Street.png",
                    "position": (538,88),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": 90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Oxford Street.png",
                    "position": (538,138),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": 90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/community_card/COMMUNITY CHEST.png",
                    "position": (538,188),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": 90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Bond Street.png",
                    "position": (538,238),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": 90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/station_card/Liverpool Street Station.png",
                    "position": (538,288),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": 90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/chance_card/CHANCE.png",
                    "position": (538,338),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": 90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Park Lane.png",
                    "position": (538,388),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": 90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/income_tax_card/INCOME TAX.png",
                    "position": (538,438),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": 90
                },
                {
                    "type": "image",
                    "search_location": "permanent",
                    "location": "map_01/assets/cards/property_card/Mayfair.png",
                    "position": (538,488),
                    "scale": ((80,50), Image.Resampling.LANCZOS),
                    "rotate": 90
                }
            ]
        }
    }
}
