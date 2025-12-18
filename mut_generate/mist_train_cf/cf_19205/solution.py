"""
QUESTION:
Create a function called "multiply_keys" that calculates the sum of all keys in a given dictionary multiplied by their values. The function should have a time complexity of O(n^2). The input dictionary will contain integers as keys and strings as values. The function should return the total sum.
"""

def multiply_keys(dictionary):
    """
    This function calculates the sum of all keys in a given dictionary multiplied by their values.
    
    Args:
        dictionary (dict): A dictionary containing integers as keys and strings as values.
    
    Returns:
        int: The total sum of all keys multiplied by their values.
    """
    total = 0
    for key in dictionary:
        for i in range(key):
            total += key
    return total