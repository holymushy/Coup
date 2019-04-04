from coup.game_state.game_state_data import CardTypes

"""
This class describes all the data about a player, and 
"""
class Player:
    player_name = ""
    cards = None
    coins = 0
    dead_cards = None

    # Creates a new player with starting config
    def __init__(self):
        pass
    
    # Requests game state for current player
    def receive_game_state(self):
        pass
    
    # Given a game state, choose an action
    def take_turn(self):
        pass
    
    # Given a game state, choose to block or not
    def decide_block(self):
        pass
    
    # Given a game state, choose to challenge or not
    def decide_challenge(self):
        pass

