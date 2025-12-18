"""
QUESTION:
Write a function named `add(a, b)` that takes two parameters and returns their sum. The function should include error handling to manage potential `TypeError` and `ValueError` exceptions. Implement the function in Python and ensure it raises the correct error messages for invalid inputs.
"""

def add(a, b):
    try:
        return a + b
    except TypeError:
        return "TypeError: You can only add numbers (both integers and floats are allowed)."
    except ValueError:
        return "ValueError: Invalid input."