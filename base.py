import os
import types

# Contains all the custom exceptions coded !
from exceptions import GameFunctioningException, OwnershipException

# Here I have not written checks for environment variables
# (except 'current_game') cause it can increase
# the loading time, slightly but still dude !


class Player:
    num_players = 0

    def __init__(self, name=None, owned_cards=None, cash=None):
        """
        Initializes a player
        """
        self.player_num = Player.num_players
        Player.num_players += 1  # For getting the default name like "Player 1"

        # Environment Variable Checks
        if not os.environ.get("current_game"):
            raise GameFunctioningException(
                "'current_game' environment variable not set !"
            )
        cg = os.environ.get("current_game")
        if Player.num_players == cg.get("num_players"):
            raise GameFunctioningException(
                """Tried to assign more players
                than allowed in current game rules."""
            )

        self.name = f"Player {self.player_num}"
        if name:
            self.name = name.title()
        self.owned_cards = (
            owned_cards
            # List of cards owned by the player (Contains objects directly)
        )
        self.cash = Cash(cash)  # A Cash object for each player's money
        self.position = 0

    def move(self, pos):
        # Move player
        self.position += pos
        # No hight limit cause it will be considered
        # in graphics relative to starting position on board

    def reset(self):
        # Reset everything including owned cards, cash and position
        if self.owned_cards:
            for i in self.owned_cards:
                i.reset()
        self.owned_cards = None
        self.cash.reset()
        self.position = 0


class Cash:
    def __init__(self, amount=None):
        """
        Cash owned by an entity (Bank, player or others)
        """
        self.amount = 0
        if amount:
            self.amount = amount

    def add(self, amount):
        # Add cash to entity's wallet
        self.amount += amount

    def remove(self, amount):
        # Remove cash from entity's wallet
        self.amount -= amount

    def reset(self):
        # Reset cash to 0
        self.amount = 0


# Functions for different implementation of Cards !


def set_owner(self, player):
    # Sets the player as the owner if it's not already set
    if self.owner:
        raise OwnershipException(self.name, self.owner.name)
    # Adds the card to the player's owned cards
    player.owned_cards.append(self)
    self.owner = player


def to(self, player):
    # Transfers the ownership from prev player to new one
    self.reset()
    self.set_owner(player)


def add_house(self):
    # Adds the houses
    if self.num_houses == 5:
        return
    self.num_houses += 1


def run_actions(self):
    # Executes the actions defined for the card
    for i in self.data.get("actions"):
        exec(i)


class Card:
    def __init__(self, name, type):
        """
        Represents cards on the board
        """
        self.name = name

        # Environment Variable Checks
        if not os.environ.get("current_game"):
            raise GameFunctioningException(
                "'current_game' environment variable not set !"
            )

        cg = os.environ.get("current_game")

        # List of all types of cards below in 'list_card_types'

        self.types_in_map = cg.get("list_card_types")
        self.rules = cg.get("card_types_data").get(
            self.type
        )  # Dictionary containing information of the card type
        self.details = cg.get("cards").get(
            name
        )  # Dictionary containing information of the card

        # Sets the type name based on value provided.
        if type < 0:
            self.type = self.types_in_map[0]
        elif type >= len(self.types_in_map):
            self.type = self.types_in_map[-1]
        else:
            self.type = self.types_in_map[type]

        # Rules based on the types information checked
        # for different functions alloted as before
        if self.rules.get("ownable"):
            self.owner = None
            self.set_owner = types.MethodType(set_owner, self)
            self.transfer_ownership = types.MethodType(to, self)
        if self.rules.get("house"):
            self.num_houses = 0
            self.add_house = types.MethodType(add_house, self)
        if self.rules.get("actions"):
            self.run_actions = types.MethodType(run_actions, self)

    def reset(self):
        """
        Resets the owner,number of houses, and
        removes the card from player's owned cards list
        """
        if self.rules.get("ownable"):
            self.owner.owned_cards.remove(self)
            self.owner = None
        if self.rules.get("house"):
            self.num_houses = 0
        current_game = os.environ.get("current_game")
        self.types_in_map = current_game.get("list_card_types")
        # The card type's list
        self.rules = current_game.get("card_types_data").get(
            self.type
        )  # Re-fetches the details of the card type
        self.details = current_game.get("cards").get(
            self.name
        )  # Re-fetches the details of the card


class Board:
    def __init__(self):

        if not os.environ.get("current_game"):
            raise GameFunctioningException(
                "'current_game' environment variable not set !"
            )

        self.board_details = os.environ.get("current_game").get(
            "board_details"
        )  # All board details in the form of string of a dictionary

        self.array_of_cards = self.board_details.get(
            "board_cards_array"
        )  # Stores the array of cards on the board
        self.left, self.top, self.right, self.bottom = self.board_details.get(
            "card_numbers"
        )  # Total number of cards on left, top, right, and bottom
        self.num_board_cards = len(
            self.array_of_cards
        )  # Total number of cards on board

        self.per_card_height = self.board_details.get(
            "per_card_height"
        )  # Width could be altering, that's why !

        self.board_dimensions = self.board_details.get("board_dimensions")

        self.player_start_position = self.board_details.get(
            "player_start_position"
        )  # Coordinates of starting position
        self.player_step_length = self.board_details.get(
            "player_step_length"
        )  # Step Length
