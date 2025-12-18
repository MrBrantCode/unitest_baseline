"""
QUESTION:
Implement a function `update_player2_message(player2_value, player2_pressed_count)` that updates `player2_message` based on the `player2_value` and handles keyboard inputs for Player 2. The function should render the updated `player2_message` on the game screen at position `(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80)` using the `blit_text` function. Ensure that the value associated with `player2_message` can be increased or decreased using the UP and DOWN keys and confirmed by pressing the ENTER key. If the confirmed value is even, `player2_message` should be in the format 'Player 2: "@" * player2_value', otherwise it should be in the format 'Player 2: "#" * player2_value'. The function should also handle the case where `player2_value` is 0.
"""

def update_player2_message(player2_value, player2_pressed_count):
    if player2_value % 2 == 0:
        player2_message = f'Player 2: {"@" * player2_value}'
    else:
        player2_message = f'Player 2: {"#" * player2_value}'
    return player2_message