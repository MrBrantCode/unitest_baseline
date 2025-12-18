"""
QUESTION:
Write a function `calculate_total_votes` that takes three lists as input: `candidates`, `votes`, and `ages`. The function should return the total number of votes for candidates who have at least 1000 votes and are aged between 18 and 30 (inclusive). The `votes` and `ages` lists are related to the candidates in the `candidates` list in the same order.
"""

def calculate_total_votes(candidates, votes, ages):
    """
    This function calculates the total number of votes for candidates who have at least 1000 votes and are aged between 18 and 30 (inclusive).
    
    Args:
        candidates (list): A list of candidate names.
        votes (list): A list of votes corresponding to the candidates.
        ages (list): A list of ages corresponding to the candidates.
    
    Returns:
        int: The total number of votes for eligible candidates.
    """
    total_votes = 0
    for i in range(len(candidates)):
        if votes[i] >= 1000 and 18 <= ages[i] <= 30:
            total_votes += votes[i]
    return total_votes