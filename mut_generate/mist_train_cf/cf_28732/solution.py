"""
QUESTION:
Implement the `getNextPlayer` function to return the next player for the next turn based on a predefined order of players. The function should take into account the current turn number (`turnNum`) and the list of players (`players`), and return the player whose turn it is next. The function should cycle back to the first player after the last player's turn.
"""

def getNextPlayer(turnNum, players):
    """
    Returns the next player for the next turn based on a predefined order of players.

    Args:
        turnNum (int): The current turn number.
        players (list): A list of players.

    Returns:
        The player whose turn it is next.
    """
    num_players = len(players)
    next_player_index = turnNum % num_players  # Get the index of the next player
    return players[next_player_index]