"""
QUESTION:
Write a function `generate_string` that takes a list of integers as input. The function should return a string where each non-negative integer in the list is concatenated, separated by a comma and a space, and prefixed with "Number: ". Negative integers should be ignored.
"""

def generate_string(numbers):
    return ", ".join(["Number: " + str(num) for num in numbers if num >= 0])