"""
QUESTION:
Write a function named `transform_data` that takes a list of integers as input and returns the transformed list after performing the following operations: remove duplicates and calculate the square of each number. The input list may contain duplicate values and the function should return a new list without modifying the original list.
"""

def transform_data(data):
    """
    This function takes a list of integers, removes duplicates, and calculates the square of each number.
    
    Args:
        data (list): A list of integers.
    
    Returns:
        list: A new list with transformed data.
    """
    return [i ** 2 for i in set(data)]