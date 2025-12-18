"""
QUESTION:
Write a function named `find_max` that takes a list of integers as input and returns the maximum value in the list. You cannot use any explicit loops, built-in functions, or methods to solve this problem.
"""

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return max(numbers[0], find_max(numbers[1:]))