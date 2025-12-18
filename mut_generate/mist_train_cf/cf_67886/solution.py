"""
QUESTION:
Create a function `product_of_odds` that takes two integer parameters `start` and `end` and returns the product of all odd numbers in the range from `start` to `end` (inclusive). The function should ignore even numbers and numbers less than 1. The function should also include input validation to check that `start` and `end` are integers, `start` is less than or equal to `end`, and both `start` and `end` are greater than 0.
"""

def product_of_odds(start, end):
    # Check that start and end are integers
    if not isinstance(start, int) or not isinstance(end, int):
        return "Both start and end values must be integers."

    # Check if start is less than end
    if start > end:
        return "Start must be less than or equal to end."

    # Check if either start or end are negative
    if start < 1 or end < 1:
        return "Both start and end must be greater than 0."

    product = 1
    for i in range(start, end + 1):  # Include end in the range
        if i % 2 != 0:  # Check if number is odd
            product *= i

    return product