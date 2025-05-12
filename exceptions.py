import os

class GameWon(Exception):
    def __init__(self):
        """
            When a player has won the match
        """
        self.message = f"Game Won by {os.environ.get('current_player')} !"
        super.__init__(self.message)

class PlayerPoor(Exception):
    def __init__(self):
        """
            When player's cash has gone below/equal to 0
        """
        self.message = f"Player {os.environ.get('current_player')} has gone in debt !"
        super.__init__(self.message)

class GameFunctioningException(Exception):
    def __init__(self,msg):
        """
            Issue in functioning of game ranging from missing/corrupt files to incorrect env vars to unintended usages
        """
        self.message = msg
        super().__init__(self.message)

class OwnershipException(Exception):
    def __init__(self,property_card):
        """
            Property Card already owned is reassigned without proper transfer
        """
        super().__init__()
        self.message = f"Property Card {property_card.name} already owned by {property_card.owner}"