"""
QUESTION:
Create a function named `sum_odd_numbers` that takes two integers, `start` and `end`, representing a range of numbers. The function should return the sum of all odd numbers within this range. The function should handle invalid inputs, where `start` and `end` are not integers, `start` is greater than `end`, or `start` is less than 1 or `end` is greater than 100. The function should be optimized for efficiency to handle large number ranges.
"""

def sum_odd_numbers(start, end):
    # Check if input is invalid
    if not (isinstance(start, int) and isinstance(end, int)):
        return "Invalid input: start and end must be integers."
    if start > end:
        return "Invalid input: start should be less or equal to end."
    if start < 1 or end > 100:
        return "Invalid input: start should be more or equal to 1 and end should be less or equal to 100."

    return sum(num for num in range(start, end+1) if num%2!=0)