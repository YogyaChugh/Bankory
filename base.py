from exceptions import * # Contains all the custom exceptions coded !
import os
import types

class Player:
    num_players = 0
    def __init__(self,name=None,owned_cards=None,cash=None):
        """
            Initializes a player
        """
        self.player_num = Player.num_players
        Player.num_players +=1 # For getting the default name like "Player 1"

        #Checks
        if not os.environ.get('current_game'):
            raise GameFunctioningException("'current_game' environment variable not set !")
        if not os.environ.get('current_game').get('num_players'):
            raise GameFunctioningException("'num_players' var not found in 'current_game' environment variable !")
        
        if Player.num_players == os.environ.get('current_game').num_players:
            raise GameFunctioningException("Tried to assign more players than allowed in current game rules.")
        

        self.name = f"Player {self.player_num}"
        if name:
            self.name = name.title()
        self.owned_cards = owned_cards  # List of cards owned by the player (Contains objects directly)
        self.cash = Cash(cash) # A Cash object for each player's money
        self.position = 0
    
    def move(self,pos):
        # Move player
        self.position += pos
        # No hight limit cause it will be considered in graphics relative to starting position on board

    def reset(self):
        # Reset everything including owned cards, cash and position
        if self.owned_cards:
            for i in self.owned_cards:
                i.reset()
        self.owned_cards = None
        self.cash.reset()
        self.position = 0

    
class Cash:
    def __init__(self,amount=None):
        """
            Cash owned by an entity (Bank, player or others)
        """
        self.amount = 0
        if amount:
            self.amount = amount
    
    def add(self,amount):
        # Add cash to entity's wallet
        self.amount += amount

    def remove(self,amount):
        # Remove cash from entity's wallet
        self.amount -= amount

    def reset(self):
        # Reset cash to 0
        self.amount = 0

# Functions for different implementation of Cards !

def set_owner(self,player):
    if self.owner is not None:
        raise OwnershipException(self.name,self.owner.name)
    player.owned_cards.append(self)
    self.owner = player

def transfer_ownership(self,player):
    self.reset()
    self.set_owner(player)

def add_house(self):
    if self.num_houses == 5:
        return
    self.num_houses += 1

def run_actions(self):
    for i in self.data.get('actions'):
        exec(i)

class Card:
    def __init__(self,name,type):
        self.name = name
        types_in_map = os.environ.get('current_game').card_types
        if type<0:
            self.type = types_in_map[0]
        elif type >= len(types_in_map):
            self.type = types_in_map[-1]
        else:
            self.type = types_in_map[type]
        self.rules = os.environ.get('current_game').card_types_file.get(self.type)
        self.details = os.environ.get('current_game').cards.get(name)
        if (self.rules.get('ownable')):
            self.owner = None
            self.set_owner = types.MethodType(set_owner,self)
            self.transfer_ownership = types.MethodType(transfer_ownership,self)
        if (self.rules.get('house')):
            self.num_houses = 0
            self.add_house = types.MethodType(add_house,self)
        if (self.rules.get('actions')):
            self.run_actions = types.MethodType(run_actions,self)
    
    def reset(self):
        if (self.rules.get('ownable')):
            self.owner.owned_cards.remove(self)
            self.owner = None
        if (self.rules.get('house')):
            self.num_houses = 0
        self.details = os.environ.get('current_game').cards.get(self.name)

class Board:
    def __init__(self):
        self.array_of_cards = os.environ.get('current_game').board_cards_array
        self.left,self.top,self.right,self.bottom = os.environ.get('current_game').board_details.get('card_numbers')
        self.num_cards = os.environ.get('current_game').total_cards
        self.num_board_cards = len(self.array_of_cards)
        self.num_special_cards = os.environ.get('current_game').board_details.get('total_special_cards')
        self.num_types_board_cards = os.environ.get('current_game').board_details.get('total_board_cards_types')
        self.num_types_special_cards = os.environ.get('current_game').board_details.get('total_special_cards_types')

        self.player_start_position = os.environ.get('current_game').board_details.get('player_start_position')
        self.player_step_length = os.environ.get('current_game').board_details.get('player_step_length')