"""
QUESTION:
Write a function 'play_game' that takes two parameters: 'player1_choice' and 'player2_choice'. Each parameter is a string that can be 'rock', 'paper', 'scissors', 'lizard', 'Spock', 'fire', 'water', 'air', or 'earth'. The function should return a string representing the outcome of the game based on the following rules: 
- Rock crushes scissors and lizard.
- Paper covers rock and disproves Spock.
- Scissors cuts paper and decapitates lizard.
- Lizard eats paper and poisons Spock.
- Spock vaporizes rock and smashes scissors.
- Fire burns rock, paper, scissors, and lizard.
- Water erodes rock, paper, scissors, and lizard.
- Air blows away rock, paper, scissors, and lizard.
- Earth absorbs rock, paper, scissors, and lizard.
- If both players choose the same option, it's a tie.
- If either player's choice is not one of the valid options, return 'Invalid input for player 1!' or 'Invalid input for player 2!' accordingly.
"""

def play_game(player1_choice, player2_choice):
    valid_choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock', 'fire', 'water', 'air', 'earth']
    
    if player1_choice not in valid_choices:
        return "Invalid input for player 1!"
    if player2_choice not in valid_choices:
        return "Invalid input for player 2!"
    
    if player1_choice == player2_choice:
        return "It's a tie!"
    
    winning_combinations = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'Spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['paper', 'Spock'],
        'Spock': ['rock', 'scissors'],
        'fire': ['rock', 'paper', 'scissors', 'lizard'],
        'water': ['rock', 'paper', 'scissors', 'lizard'],
        'air': ['rock', 'paper', 'scissors', 'lizard'],
        'earth': ['rock', 'paper', 'scissors', 'lizard']
    }
    
    if player2_choice in winning_combinations[player1_choice]:
        return 'Player 1 wins!'
    else:
        return 'Player 2 wins!'