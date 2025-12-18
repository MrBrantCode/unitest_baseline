"""
QUESTION:
Write a function 'play_game' that takes two parameters 'player1_choice' and 'player2_choice'. Both parameters are strings that can be 'rock', 'paper', 'scissors', 'lizard', 'Spock', 'fire', 'water', 'air', or 'earth'. The function should return a string representing the outcome of the game based on the following rules: 
- Rock crushes scissors and lizard. 
- Paper covers rock and disproves Spock. 
- Scissors cuts paper and decapitates lizard. 
- Lizard eats paper and poisons Spock. 
- Spock vaporizes rock and smashes scissors. 
- Fire burns rock, paper, scissors, and lizard. 
- Water erodes rock, paper, scissors, and lizard. 
- Air blows away rock, paper, scissors, and lizard. 
- Earth absorbs rock, paper, scissors, and lizard. 
If player 1 wins, return 'Player 1 wins!'. If player 2 wins, return 'Player 2 wins!'. If it's a tie, return 'It's a tie!'. If either player's input is invalid, return an error message indicating which player's input is invalid.
"""

def play_game(player1_choice, player2_choice):
    valid_choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock', 'fire', 'water', 'air', 'earth']
    
    if player1_choice not in valid_choices:
        return "Invalid input for player 1!"
    if player2_choice not in valid_choices:
        return "Invalid input for player 2!"
    
    if player1_choice == player2_choice:
        return "It's a tie!"
    
    if player1_choice == 'rock':
        if player2_choice == 'scissors' or player2_choice == 'lizard':
            return 'Player 1 wins!'
        else:
            return 'Player 2 wins!'
    
    if player1_choice == 'paper':
        if player2_choice == 'rock' or player2_choice == 'Spock':
            return 'Player 1 wins!'
        else:
            return 'Player 2 wins!'
    
    if player1_choice == 'scissors':
        if player2_choice == 'paper' or player2_choice == 'lizard':
            return 'Player 1 wins!'
        else:
            return 'Player 2 wins!'
    
    if player1_choice == 'lizard':
        if player2_choice == 'paper' or player2_choice == 'Spock':
            return 'Player 1 wins!'
        else:
            return 'Player 2 wins!'
    
    if player1_choice == 'Spock':
        if player2_choice == 'rock' or player2_choice == 'scissors':
            return 'Player 1 wins!'
        else:
            return 'Player 2 wins!'
    
    if player1_choice == 'fire' or player1_choice == 'water' or player1_choice == 'air' or player1_choice == 'earth':
        return 'Player 1 wins!'
    
    return 'Player 2 wins!'