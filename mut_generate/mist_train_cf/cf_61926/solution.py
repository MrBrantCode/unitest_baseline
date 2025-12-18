"""
QUESTION:
Create a function named `sort_descending` that takes a list of numbers in different forms (whole numbers, fractions, and decimal numbers) as input and returns the numbers in descending order. The input list may contain fractions, which should be converted to decimal numbers before sorting. Use Python's built-in functions to achieve this. The function should return a list of numbers in descending order.
"""

def sort_descending(numbers):
    """
    This function takes a list of numbers in different forms (whole numbers, fractions, and decimal numbers) 
    as input and returns the numbers in descending order.
    
    Args:
    numbers (list): A list of numbers in different forms
    
    Returns:
    list: A list of numbers in descending order
    """
    return sorted(numbers, reverse=True)