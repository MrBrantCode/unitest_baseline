"""
QUESTION:
Write a function `filter_numbers_by_threshold` that takes a list of integers and an upper threshold as input, and returns a new list containing only the numbers from the original list that do not exceed the upper threshold.
"""

def filter_numbers_by_threshold(numbers, upper_threshold):
    """
    This function filters a list of numbers based on a given upper threshold.
    
    Args:
    numbers (list): A list of integers.
    upper_threshold (int): The upper limit for filtering numbers.
    
    Returns:
    list: A new list containing only the numbers from the original list that do not exceed the upper threshold.
    """
    return [num for num in numbers if num <= upper_threshold]