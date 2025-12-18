"""
QUESTION:
Create a function `unique_assemblage` that takes a chronologically ordered list of unique natural numbers as input and returns a dictionary where each number from the list is paired with its index.
"""

def unique_assemblage(numbers):
    """
    Creates a dictionary where each number from the input list is paired with its index.

    Args:
    numbers (list): A chronologically ordered list of unique natural numbers.

    Returns:
    dict: A dictionary where each number from the list is paired with its index.
    """
    return {num: idx for idx, num in enumerate(numbers)}