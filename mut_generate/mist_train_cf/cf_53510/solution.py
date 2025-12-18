"""
QUESTION:
Write a function `harmonic_mean(numbers)` that calculates the harmonic mean of a list of non-zero integers. The function should not handle user input directly. Instead, it should assume that the input list `numbers` is valid and contains only non-zero integers. The function should return the harmonic mean of the input numbers.

Restrictions: The input list `numbers` will only contain non-zero integers.
"""

def harmonic_mean(numbers):
    """
    Calculate the harmonic mean of a list of non-zero integers.
    
    Args:
        numbers (list): A list of non-zero integers.
    
    Returns:
        float: The harmonic mean of the input numbers.
    """
    return len(numbers) / sum(1 / num for num in numbers)