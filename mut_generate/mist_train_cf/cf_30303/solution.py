"""
QUESTION:
Write a function `determine_outcome(player_choice, ia_choice)` that takes two parameters, `player_choice` and `ia_choice`, each representing a choice of rock, paper, or scissor. The function should return a string indicating the outcome of the game, either 'victory', 'defeat', or 'draw', based on the game's rules: rock beats scissor, scissor beats paper, and paper beats rock. If the choices are the same, the game is a draw.
"""

def determine_outcome(player_choice, ia_choice):
    if player_choice == 'rock':
        if ia_choice == 'rock':
            return 'draw'
        elif ia_choice == 'scissor':
            return 'victory'
        elif ia_choice == 'paper':
            return 'defeat'
    elif player_choice == 'scissor':
        if ia_choice == 'rock':
            return 'defeat'
        elif ia_choice == 'scissor':
            return 'draw'
        elif ia_choice == 'paper':
            return 'victory'
    elif player_choice == 'paper':
        if ia_choice == 'rock':
            return 'victory'
        elif ia_choice == 'scissor':
            return 'defeat'
        elif ia_choice == 'paper':
            return 'draw'