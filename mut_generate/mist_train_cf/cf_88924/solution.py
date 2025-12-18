"""
QUESTION:
Write a function `generate_string(numbers)` that takes a list of integers as input and returns a string where each non-negative integer is converted to a string, prefixed with "Number: ", and all the prefixed strings are concatenated, separated by a comma and a space. The function should ignore any negative integers in the list.
"""

def generate_string(numbers):
    return ", ".join(["Number: " + str(num) for num in numbers if num >= 0])