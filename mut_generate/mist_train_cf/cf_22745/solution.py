"""
QUESTION:
Create a function named `calculate_sum` that takes a list of numbers as input and returns the sum of those numbers without using the built-in `sum()` function or any loops. The function should use recursion to calculate the sum.
"""

def calculate_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + calculate_sum(numbers[1:])