"""
QUESTION:
Create a function called `determine_winner` that takes two parameters: `player` and `computer`, which represent the player's and the computer's choices, respectively, as integers (0 for rock, 1 for paper, 2 for scissors). The function should return a string indicating the result of the game: 'It's a tie!', 'Computer wins!', or 'Player wins!'. The function should not take any user input or generate random numbers.
"""

def determine_winner(player, computer):
    """
    Determine the winner of a game of rock, paper, scissors.

    Args:
    player (int): The player's choice (0 for rock, 1 for paper, 2 for scissors).
    computer (int): The computer's choice (0 for rock, 1 for paper, 2 for scissors).

    Returns:
    str: The result of the game ('It's a tie!', 'Computer wins!', or 'Player wins!').
    """
    if computer == player:
        return 'It\'s a tie!'
    elif (computer - player) % 3 == 1:
        return 'Computer wins!'
    else:
        return 'Player wins!'