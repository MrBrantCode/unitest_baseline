"""
QUESTION:
Write a function `find_max` that takes a list of integers as input and returns the maximum value, without using explicit loops, built-in functions (except for `len`), or methods. The function should be able to handle lists with at least one element.
"""

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return max(numbers[0], find_max(numbers[1:]))