"""
QUESTION:
Consider a game where two players take alternate turns removing 1, 2, or 3 stones from a pile of n stones. The player who removes the last stone wins. Write a function `count_first_player_wins` to calculate the number of values of n (1 ≤ n ≤ 1,000,000) for which the first player can force a win.
"""

def count_first_player_wins(n):
    """
    Calculate the number of values of n for which the first player can force a win.
    
    Args:
    n (int): The upper limit of the range of values to check.
    
    Returns:
    int: The number of values for which the first player can force a win.
    """
    return n - n//4