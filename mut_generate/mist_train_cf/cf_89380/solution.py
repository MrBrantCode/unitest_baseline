"""
QUESTION:
Write a function named `compute_median` that takes a list of numbers as input and returns the median as an integer, rounded to the nearest integer. Implement the solution in a single line of code.
"""

def compute_median(numbers):
    return int(sorted(numbers)[len(numbers) // 2]) if len(numbers) % 2 else int(sum(sorted(numbers)[len(numbers) // 2 - 1:len(numbers) // 2 + 1]) / 2)