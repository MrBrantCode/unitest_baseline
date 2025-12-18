"""
QUESTION:
Create a function `filter_numbers` that takes a list of integers as input and returns a new list with all numbers divisible by 3 and 4 removed, and the remaining numbers sorted in descending order. The function should not modify the original list.
"""

def filter_numbers(numbers):
    """
    This function filters out all numbers divisible by 3 and 4 from the given list of integers and returns the remaining numbers in descending order.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    list: A new list of integers with all numbers divisible by 3 and 4 removed, sorted in descending order.
    """
    return sorted([num for num in numbers if num % 3 != 0 and num % 4 != 0], reverse=True)