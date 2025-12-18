"""
QUESTION:
Write a Python function `problematic_function` that demonstrates a division by zero error when the input value is zero. The function should be called in a `try` block, and an `except` block should be used to catch the resulting exception and print an error message.
"""

def problematic_function(val):
    result = 10/val   # this will cause division by zero error if val=0
    return result