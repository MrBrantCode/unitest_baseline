"""
QUESTION:
Write a function 'play_game' that takes two parameters, 'player1_choice' and 'player2_choice', both representing the choice of player 1 and player 2 in a game of rock paper scissors. The function should return a string representing the outcome of the game. The choices can be 'rock', 'paper', or 'scissors'. If the input is invalid, return an error message.
"""

def entrance(player1_choice, player2_choice):
    valid_choices = ['rock', 'paper', 'scissors']
    
    # Check if the choices are valid
    if player1_choice not in valid_choices:
        return 'Invalid input for player 1!'
    if player2_choice not in valid_choices:
        return 'Invalid input for player 2!'
    
    # Check the outcome of the game
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or (player1_choice == 'paper' and player2_choice == 'rock') or (player1_choice == 'scissors' and player2_choice == 'paper'):
        return 'Player 1 wins!'
    else:
        return 'Player 2 wins!'