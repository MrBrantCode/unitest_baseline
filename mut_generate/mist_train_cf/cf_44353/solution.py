"""
QUESTION:
Write a function named `factorial_of_list` that calculates the factorial of each integer in a given list. The list should contain only integers from 1 to 1000 and its length should not exceed 1000. If the input is not a list, the list contains non-integer items, or the list or its items are out of range, the function should return a meaningful error message.
"""

import math

def factorial_of_list(l):
    # Check if it's not a list
    if not isinstance(l, list):
        return "Error: Input is not a list."

    # Check if list exceeding length
    if len(l) > 1000:
        return "Error: The list is too long. It should not exceed 1000 items."

    # Calculate factorials
    factorials = []
    for item in l:
        # Check if item is not an integer
        if not isinstance(item, int):
            return f"Error: List contains non-integer item: {item}"

        # Check if item is out of range
        if item < 1 or item > 1000:
            return f"Error: The integer ({item}) should be in the range from 1 to 1000."

        # Calculate and append factorial
        factorials.append(math.factorial(item))

    return factorials