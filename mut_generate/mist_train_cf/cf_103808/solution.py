"""
QUESTION:
Write a function `count_valid_fruits` that takes two parameters: `items` (a list of strings representing the items to be counted) and `valid_fruits` (a list of strings representing the valid fruits). The function should return the total count of valid fruits in the `items` list. A valid fruit is an item that exists in the `valid_fruits` list. The function should skip items that are not valid fruits.
"""

def count_valid_fruits(items, valid_fruits):
    """
    Returns the total count of valid fruits in the items list.
    
    Parameters:
    items (list): A list of strings representing the items to be counted.
    valid_fruits (list): A list of strings representing the valid fruits.
    
    Returns:
    int: The total count of valid fruits.
    """
    total = 0
    for item in items:
        if item in valid_fruits:
            total += 1  # Increment count for each valid fruit
    return total