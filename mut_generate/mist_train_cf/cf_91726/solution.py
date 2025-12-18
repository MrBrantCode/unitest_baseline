"""
QUESTION:
Write a function named `calculate_average` that calculates the average of all elements in a given array of integers. The array will contain at least 5 elements and at most 100 elements, and each element will be a positive integer between 1 and 1000, inclusive. The function should return the average rounded to the nearest integer.
"""

def calculate_average(arr):
    """
    This function calculates the average of all elements in a given array of integers.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The average of all elements in the array, rounded to the nearest integer.
    """
    return round(sum(arr) / len(arr))