"""
QUESTION:
Create a function named `play_round` that takes two parameters, `player1` and `player2`, representing the choices of two players in a Rock-Paper-Scissors game. The function should return the outcome of the round, either "player1", "player2", or "draw", based on the game's rules: rock beats scissors, scissors beats paper, and paper beats rock.
"""

def play_round(player1, player2):
    """
    This function determines the outcome of a Rock-Paper-Scissors round.

    Args:
        player1 (str): The choice of the first player.
        player2 (str): The choice of the second player.

    Returns:
        str: The outcome of the round, either "player1", "player2", or "draw".
    """
    if player1 == player2:
        return "draw"
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
        return "player1"
    else:
        return "player2"