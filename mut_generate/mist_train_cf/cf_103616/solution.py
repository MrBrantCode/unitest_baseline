"""
QUESTION:
Write a function `compute_mean` that calculates the mean of a given list of numbers and returns the result as a floating-point number. The function should utilize a list comprehension to achieve this. The input will be a list of numbers and the output should be a floating-point number. The function should handle cases where the input list is empty.
"""

def compute_mean(numbers):
    """
    Calculates the mean of a given list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The mean of the input list as a floating-point number.
    """
    if not numbers:
        return 0.0
    return sum(float(x) for x in numbers) / len(numbers)