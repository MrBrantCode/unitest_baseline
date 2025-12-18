"""
QUESTION:
Write a function named `calculate_mean` that takes a list of numbers as input and returns the mean of those numbers without using any built-in functions or libraries for calculating the mean.
"""

def calculate_mean(numbers):
    """
    This function calculates the mean of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The mean of the numbers in the list.
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)