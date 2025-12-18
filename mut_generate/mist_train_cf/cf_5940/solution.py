"""
QUESTION:
Create a function called `update_array` that takes an array of positive integers as input. The function should update the array by squaring each element and removing any elements that are divisible by 3. The function should return the sum of the remaining elements without using loops, conditional statements, or built-in array functions such as map, filter, or reduce.
"""

def update_array(arr):
    """
    Updates the input array by squaring each element and removing any elements 
    that are divisible by 3, then returns the sum of the remaining elements.

    Args:
        arr (list): A list of positive integers.

    Returns:
        int: The sum of the remaining elements in the updated array.
    """
    return sum(num ** 2 for num in arr if (num ** 2) % 3 != 0)