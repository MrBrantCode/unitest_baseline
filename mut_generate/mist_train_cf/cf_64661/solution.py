"""
QUESTION:
Write a function named `multiply` that takes two integers as input and returns their product. The function should handle potential zero division errors. Then, write a program that reads a list of space-separated integers from the user, applies the `multiply` function to all elements in the list from left to right using the `reduce` function, and prints the result. The program should be compatible with Python 3 and should import the `reduce` function from the `functools` module if necessary.
"""

from functools import reduce

def multiply(x, y):
    # Managing zero division
    if y == 0:
        return 0
    return x*y