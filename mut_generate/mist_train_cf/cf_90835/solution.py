"""
QUESTION:
Create a custom exception called `CustomException` in Python that inherits from the built-in `Exception` class. This exception should be raised when a division by zero occurs in the `divide_numbers` function, which takes two parameters `a` and `b` and returns their division result. The `divide_numbers` function should raise the `CustomException` with the error message "Division by zero is not allowed." when `b` is zero. Use a try-except block to catch and handle the `CustomException` by printing an error message.
"""

class CustomException(Exception):
    pass

def divide_numbers(a, b):
    if b == 0:
        raise CustomException("Division by zero is not allowed.")
    return a / b