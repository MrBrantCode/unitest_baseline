"""
QUESTION:
Write a function named sum_divisible_by_three that takes an array of integers as input and returns the sum of the elements that are greater than or equal to 10 and are divisible by 3. If no such elements exist, return -1.
"""

def sum_divisible_by_three(arr):
    """
    Returns the sum of elements in the array that are greater than or equal to 10 and are divisible by 3.
    If no such elements exist, returns -1.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The sum of elements meeting the condition or -1 if no such elements exist.
    """
    return sum(num for num in arr if num >= 10 and num % 3 == 0) or -1