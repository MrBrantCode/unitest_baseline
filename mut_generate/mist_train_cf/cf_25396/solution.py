"""
QUESTION:
Write a function `sum_between_range` to calculate the sum of all integers between two given numbers (inclusive). The function should take two integers as input and return the sum. The range should be from the first number to the second number (inclusive) if the first number is less than or equal to the second number; otherwise, the range should be from the second number to the first number (inclusive).
"""

def sum_between_range(a, b):
    """
    Calculate the sum of all integers between two given numbers (inclusive).
    
    The range is from the first number to the second number (inclusive) if the first number is less than or equal to the second number; 
    otherwise, the range is from the second number to the first number (inclusive).
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of all integers between two given numbers (inclusive).
    """
    return sum(range(min(a, b), max(a, b) + 1))