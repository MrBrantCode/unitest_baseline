"""
QUESTION:
Implement a function `extract_and_sum_numbers` that takes an alphanumeric string as input. The function should extract all the numbers from the string, store them in a list, sort the list in ascending order, and return the sum of the numbers. The solution should be efficient, avoiding any unnecessary time or space complexity.
"""

import re

def extract_and_sum_numbers(s):
    """
    This function takes an alphanumeric string, extracts numbers, sorts them in ascending order and returns their sum.

    Args:
        s (str): The input alphanumeric string.

    Returns:
        int: The sum of the extracted numbers.
    """
    # Use regex to find all occurrences of digits in the string
    numbers = re.findall('\d+', s)

    # Convert each number from string to integer
    numbers = list(map(int, numbers))

    # Sort the numbers
    numbers.sort()

    # Calculate the sum of the numbers
    total = sum(numbers)

    return total