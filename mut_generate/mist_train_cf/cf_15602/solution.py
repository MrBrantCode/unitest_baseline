"""
QUESTION:
Write a function `absolute_difference(num1, num2)` that calculates the absolute difference between two numbers using basic arithmetic operations and comparisons a maximum of two times. The function should have a time complexity of O(1) and use a constant amount of space.
"""

def absolute_difference(num1, num2):
    diff = num1 - num2  # First comparison and subtraction
    if diff < 0:
        diff = -diff
    return diff