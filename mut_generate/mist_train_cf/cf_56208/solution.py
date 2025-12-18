"""
QUESTION:
Write a function called `squared_discrepancies_sum` that calculates the sum of squared differences between each number in the input list and the mean of the list. The function should take a list of numbers as input and return the sum of squared discrepancies. The input list is guaranteed to be non-empty.
"""

def squared_discrepancies_sum(numbers):
    """
    Calculate the sum of squared differences between each number in the input list and the mean of the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The sum of squared discrepancies.
    """
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers)