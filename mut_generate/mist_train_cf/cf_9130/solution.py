"""
QUESTION:
Write a function called `calculate_sum` that takes in a list of numbers as input, which can be a nested list, and returns the sum of all the numbers in the list.

The function should meet the following requirements and constraints:
- Handle both positive and negative integers and floating-point numbers.
- Handle empty lists, non-numeric elements, and duplicate numbers.
- Ignore non-numeric elements and do not use built-in sum() or library functions.
- Use a loop for incremental sum calculation.
- Handle large input lists efficiently without memory or performance issues.
- Return the sum as a floating-point number, rounded to 2 decimal places.
- Handle numbers close to the maximum and minimum representable values without overflow or underflow errors.
"""

def calculate_sum(lst):
    total_sum = 0.0
    for element in lst:
        if isinstance(element, list):
            total_sum += calculate_sum(element)
        elif isinstance(element, (int, float)):
            total_sum += element
    return round(total_sum, 2)