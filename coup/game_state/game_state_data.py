from enum import Enum
"""
This class represents the entirety of game state.
Should be save-able, serializable, and load-able.
"""
class GameStateData:
    num_players = 0
    curr_turn_index = 0 #who's turn it is for playing
    curr_chal_index = 0 #who's turn it is for challenges
    players = []
    deck = None
    turn_history = None

    # Creates a starting game state
    def __init__(self, num_players):
        pass
    
    # Exports the data to some format
    def export(self):
        pass


CardTypes = Enum("CardTypes", "Null Assa Amba Capt Cont Duke")

class Deck:
    remaining_cards = []

    # Creates a starting deck
    def __init__(self):
        pass