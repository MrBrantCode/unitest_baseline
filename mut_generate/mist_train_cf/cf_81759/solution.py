"""
QUESTION:
Create a function called `calculate_median` that takes a list of decimal numbers as input and returns the median of the list. The list can be of variable length and may contain non-numerical elements or null values. The function should handle these cases by filtering out non-numerical and null values, and return an error message if the list is empty or contains no numerical values.
"""

def calculate_median(numbers):
    """
    Calculate the median of a list of decimal numbers.

    Args:
        numbers (list): A list of decimal numbers.

    Returns:
        The median of the list, or an error message if the list is empty or contains no numerical values.
    """

    # Filter out non-numerical and null values
    numbers = [i for i in numbers if isinstance(i, (int, float))]

    n = len(numbers)

    # Check if the list is empty or contains no numerical values
    if n == 0:
        return "Error: No numerical values found in array."

    # Sort the list
    numbers.sort()

    # Calculate the median
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]

    return median