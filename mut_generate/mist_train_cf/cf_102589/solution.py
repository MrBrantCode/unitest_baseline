"""
QUESTION:
Write a function `harmonic_mean` that calculates the harmonic mean of a given list of positive numbers. The harmonic mean is the reciprocal of the arithmetic mean of the reciprocals of the numbers in the list. The input list will only contain positive numbers.
"""

def harmonic_mean(numbers):
    """
    This function calculates the harmonic mean of a given list of positive numbers.
    
    Parameters:
    numbers (list): A list of positive numbers.
    
    Returns:
    float: The harmonic mean of the given list of numbers.
    """
    reciprocal_sum = sum(1/x for x in numbers)
    return len(numbers) / reciprocal_sum