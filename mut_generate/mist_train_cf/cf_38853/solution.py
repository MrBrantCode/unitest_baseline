"""
QUESTION:
Implement the function `determine_game_phase` that takes the number of player pieces and the current phase as input and returns the correct game phase based on the rules of the game. The function should return 'FLY' if the number of player pieces is 3 and the current phase is not 'INIT', otherwise it should return the current phase.
"""

def determine_game_phase(num_pieces, current_phase):
    if num_pieces == 3 and current_phase != 'INIT':
        return 'FLY'
    else:
        return current_phase