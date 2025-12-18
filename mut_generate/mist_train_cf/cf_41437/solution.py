"""
QUESTION:
Write a function named `three_smallest_numbers` that takes a list of integers as input, sorts the list in ascending order, and returns the three smallest numbers as a string separated by spaces. The input list contains at least three integers.
"""

def three_smallest_numbers(numbers):
    numbers.sort()
    return ' '.join(map(str, numbers[:3]))