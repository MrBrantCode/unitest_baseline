"""
QUESTION:
Create a function `play_game` that takes in two parameters, `player1_choice` and `player2_choice`, both strings representing the choices of players 1 and 2 respectively. The function should return a string representing the outcome of the game. 

`player1_choice` and `player2_choice` can be 'rock', 'paper', 'scissors', 'lizard', or 'Spock'. If either choice is invalid, the function should return an error message. The game's rules are as follows: rock crushes scissors and lizard, paper covers rock and disproves Spock, scissors cuts paper and decapitates lizard, lizard eats paper and poisons Spock, and Spock vaporizes rock and smashes scissors.
"""

def play_game(player1_choice, player2_choice):
    valid_choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock']

    if player1_choice not in valid_choices:
        return 'Invalid input for player 1!'
    if player2_choice not in valid_choices:
        return 'Invalid input for player 2!'

    if player1_choice == player2_choice:
        return "It's a tie!"

    if (player1_choice == 'rock' and player2_choice == 'scissors') or (player1_choice == 'rock' and player2_choice == 'lizard'):
        return 'Player 1 wins!'
    elif (player1_choice == 'paper' and player2_choice == 'rock') or (player1_choice == 'paper' and player2_choice == 'Spock'):
        return 'Player 1 wins!'
    elif (player1_choice == 'scissors' and player2_choice == 'paper') or (player1_choice == 'scissors' and player2_choice == 'lizard'):
        return 'Player 1 wins!'
    elif (player1_choice == 'lizard' and player2_choice == 'paper') or (player1_choice == 'lizard' and player2_choice == 'Spock'):
        return 'Player 1 wins!'
    elif (player1_choice == 'Spock' and player2_choice == 'rock') or (player1_choice == 'Spock' and player2_choice == 'scissors'):
        return 'Player 1 wins!'
    else:
        return 'Player 2 wins!'