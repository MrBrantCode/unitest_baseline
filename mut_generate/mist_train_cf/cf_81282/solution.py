"""
QUESTION:
Write a function named `multiply_numbers` that takes a string of space-separated integers as input, splits the string into integers, and returns their product. The function should handle potential zero division errors by returning an error message. The function should be compatible with Python 3 syntax.
"""

from functools import reduce

def multiply_numbers(input_str):
    try:
        data = list(map(int, input_str.split()))
        return reduce(lambda x, y: x*y, data)
    except ZeroDivisionError:
        return 'Error: Division by zero'