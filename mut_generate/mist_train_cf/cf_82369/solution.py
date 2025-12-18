"""
QUESTION:
Given a set of 'n' unique balls and 2 indistinguishable boxes, write a function 'count_arrangements' that calculates the number of different arrangements to distribute the balls into the boxes, considering all possible combinations.
"""

def count_arrangements(n):
    """
    Calculate the number of different arrangements to distribute 'n' unique balls into 2 indistinguishable boxes.

    Args:
        n (int): The number of unique balls.

    Returns:
        int: The number of different arrangements.
    """
    # Calculate total combinations
    total_combinations = 2 ** n
    
    # Subtract combinations where balls are all in one box
    total_combinations -= 2
    
    return total_combinations