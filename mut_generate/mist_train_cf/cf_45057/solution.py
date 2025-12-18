"""
QUESTION:
Write a function `sortVegetables` that takes a list of vegetable names as input and returns the list in reverse alphabetical order.
"""

def sortVegetables(vegetables):
    """
    This function takes a list of vegetable names and returns the list in reverse alphabetical order.

    Args:
        vegetables (list): A list of vegetable names

    Returns:
        list: The input list in reverse alphabetical order
    """
    return sorted(vegetables, reverse=True)