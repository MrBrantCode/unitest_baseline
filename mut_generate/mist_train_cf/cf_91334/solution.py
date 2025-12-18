"""
QUESTION:
Write a function `calculate_odd_average` that takes a list of integers as input, calculates the sum of all odd elements in the list without using built-in sum functions or the modulus operator (%), and returns the average of these odd elements.
"""

def calculate_odd_average(numbers):
    """
    This function calculates the average of all odd elements in the given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The average of all odd elements in the list.
    """
    odd_sum = 0
    odd_count = 0

    for num in numbers:
        odd_sum = odd_sum + (num & 1) * num  # bitwise AND operator with 1 to check if the number is odd
        odd_count = odd_count + (num & 1)    # increment odd_count if the number is odd

    if odd_count > 0:
        return odd_sum / odd_count
    else:
        return 0.0