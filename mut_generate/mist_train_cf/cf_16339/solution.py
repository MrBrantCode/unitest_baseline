"""
QUESTION:
Create a function named `calculate_average` to calculate the average of numbers in a list until the sum of the numbers exceeds or equals a given threshold. The function should take two parameters: `values` (a list of numbers) and `threshold` (the maximum sum). The function should return the calculated average.
"""

def calculate_average(values, threshold):
    """
    Calculate the average of numbers in a list until the sum of the numbers exceeds or equals a given threshold.

    Args:
        values (list): A list of numbers.
        threshold (int): The maximum sum.

    Returns:
        float: The calculated average.
    """
    total = 0
    count = 0
    for value in values:
        total += value
        count += 1
        if total >= threshold:
            break
    return total / count