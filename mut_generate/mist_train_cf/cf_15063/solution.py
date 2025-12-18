"""
QUESTION:
Write a recursive function `sum_positive_numbers` that takes a list of integers as input, ignores any negative numbers in the list, and returns the sum of all positive numbers. The function should handle the case when the input list is empty and should not use any loops.
"""

def sum_positive_numbers(numbers):
    if len(numbers) == 0:
        return 0
    elif numbers[0] < 0:
        return sum_positive_numbers(numbers[1:])
    else:
        return numbers[0] + sum_positive_numbers(numbers[1:])