"""
QUESTION:
Write a function `safe_divide` that takes a number `num` as input and returns the result of 1 divided by `num`. If `num` is zero, the function should catch the exception, print an error message, and return -1.
"""

def safe_divide(num):
    try:
        return 1 / num
    except ZeroDivisionError:
        print("An error occurred: Division by zero is undefined.")
        return -1