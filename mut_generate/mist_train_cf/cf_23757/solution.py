"""
QUESTION:
Write a function `myDict` that takes a list of integers as input and returns a dictionary where each integer in the list is a key and its corresponding value is the square of the key.
"""

def myDict(nums):
    """
    Returns a dictionary where each integer in the input list is a key and its corresponding value is the square of the key.

    Args:
        nums (list): A list of integers.

    Returns:
        dict: A dictionary with integers as keys and their squares as values.
    """
    result = {}
    for i in nums:
        result[i] = i**2
    return result