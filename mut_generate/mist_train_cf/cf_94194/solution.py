"""
QUESTION:
Write a function `calculate_average` that calculates the average of a list of numbers until their sum exceeds a certain threshold. The function should take in two parameters: a list of numbers `values` and a number `threshold`. The function should return the average of the numbers in the list until their sum exceeds or equals the threshold.
"""

def calculate_average(values, threshold):
    """
    Calculate the average of a list of numbers until their sum exceeds a certain threshold.

    Args:
        values (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        float: The average of the numbers in the list until their sum exceeds or equals the threshold.
    """
    total = 0
    count = 0
    for value in values:
        total += value
        count += 1
        if total >= threshold:
            break

    return total / count if count > 0 else 0