"""
QUESTION:
Write a function `multiply(a, b)` that takes two inputs and returns their product. The function should handle both integer and float inputs, and print an error message and return `None` if either input is neither an integer nor a float.
"""

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Error: Inputs must be integers or floats.")
        return None
    return a * b