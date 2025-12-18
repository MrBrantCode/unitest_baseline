"""
QUESTION:
Write a function named `find_min` that takes a list of numbers as input, which can include integers and floating-point numbers, both positive and negative. The function should return the smallest number in the list. You are not allowed to use the built-in `min()` function.
"""

def find_min(numbers):
    min_val = numbers[0]  # Start with the first value
    for i in numbers:
        if i < min_val:   # If we find a number which is less than our current minimum
            min_val = i   # We replace it
    return min_val