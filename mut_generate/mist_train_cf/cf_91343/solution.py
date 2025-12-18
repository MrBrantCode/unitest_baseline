"""
QUESTION:
Write a function named `calculate_sum` that takes a list of numbers as input and returns the sum of all numbers in the list. The function should not use any built-in sum function or loops.
"""

def calculate_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + calculate_sum(numbers[1:])