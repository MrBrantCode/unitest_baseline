"""
QUESTION:
Write a function `update_scores` that takes the current scores of two players and the winner of a round as input, and returns the updated scores. The function should take into account the following rules:
- Each player starts with 10 points.
- The loser of a round loses 1 point, and the winner gains 1 point.
- In case of a tie, no points are gained or lost.
- The game ends when one player reaches 0 points or 20 points.
"""

def update_scores(player1_score, player2_score, winner):
    """
    Updates the scores of two players based on the winner of a round.

    Args:
    player1_score (int): The current score of player 1.
    player2_score (int): The current score of player 2.
    winner (str): The winner of the round, either 'player1', 'player2', or 'tie'.

    Returns:
    tuple: The updated scores of player 1 and player 2.
    """

    # Update scores based on the winner
    if winner == 'player1':
        player1_score += 1
        player2_score -= 1
    elif winner == 'player2':
        player1_score -= 1
        player2_score += 1
    # No points are gained or lost in case of a tie
    elif winner == 'tie':
        pass

    # Ensure scores do not go below 0
    player1_score = max(player1_score, 0)
    player2_score = max(player2_score, 0)

    return player1_score, player2_score