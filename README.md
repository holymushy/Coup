### Coup

This is our first project!
KwokKwokKwokKwokKwokKwokKwok

# Design Architecture

Status: In Progress

# Design for Coup

- `class GameState`
- `abstract class / interface Role`
- `class Captain, Contessa, Assassin, Duke, Ambassador **inherit / implement** Role`

- `class GUI`
- `class Main`
- `class Player`
- Minimal description of Gamestate for rendering
    - Num players total
    - Current player for turn - int
    - Current player for challenge - int
    - Player - Struct
        - (Name?) - string
        - Cards - Capt, Cont, Assa, Duke, Amba - int[2]
        - Coins - int
        - Lost lives - int[2]
    - Deck
        - (Remaining cards)? - int[5]
    - (Turn history) - string - (should be parseable to recreate gamestate)

Notes - game_state needs to broadcast actions and history and unicast action requests

- `class Game_state`
    - `def play() # While num players > 1, curr player take turn, resolve, set player to next player`
    - `def start_game() # Prompt game creator for game setup parameters`
    - `def retrieve_state_for_player() # Returns the information a player has`
    - `def resolve_action() # Resolves the effects of an action`
- `class Player`
    - `def receive_game_state() # Receive game_state update from game_state`
    - `def take_turn() # Given a game state, choose an action (and a target)`
    - `def decide_blocking() # Given a game state, choose whether or not to block`
    - `def decide_challenge() # Given a game state, choose whether or not to challenge`
- `class GUI`
    - `def render_game_state() # Renders game state as viewed by a player`
    - `def display_input_action() # Give user the take_turn prompt`
    - `def display_input_block() # Give user the decide_blocking prompt`
    - `def display_input_challenge() # Give user the decide_challenge prompt`