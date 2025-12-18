"""
QUESTION:
Write a function named `sum_squared_multiplied_items` that takes a 2D array as input. For each item in the array, multiply it by its index (where the index is calculated as i * len(row) + j for a 2D array), then square the result. Return the sum of all these squared multiplied items.
"""

def sum_squared_multiplied_items(arr):
    """
    This function calculates the sum of the squared multiplied items in a 2D array.
    
    For each item in the array, it multiplies the item by its index (where the index is 
    calculated as i * len(row) + j for a 2D array), then squares the result.

    Args:
        arr (list): A 2D array.

    Returns:
        int: The sum of the squared multiplied items.
    """
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            multiplied_item = arr[i][j] * (i * len(arr[i]) + j)
            squared_multiplied_item = multiplied_item ** 2
            result += squared_multiplied_item
    return result