"""
QUESTION:
Write a function called `find_maximum` that takes five numbers as input and returns the maximum of the five numbers without using the built-in `max()` function and without using any conditional statements. The function should be able to handle any set of five numbers.
"""

def find_maximum(num1, num2, num3, num4, num5):
    numbers = [num1, num2, num3, num4, num5]
    numbers.sort()
    return numbers[-1]