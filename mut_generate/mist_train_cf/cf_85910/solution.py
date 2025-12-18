"""
QUESTION:
Write a function named `describe_input` that takes a string as input and returns a string describing whether the input string represents an integer, a floating-point number, or a string. The function should return 'integer' if the input string can be converted to an integer, 'floating-point number' if it can be converted to a float but not an integer, and 'string' otherwise.
"""

def describe_input(value):
    try:
        int(value)
        return 'integer'
    except ValueError:
        try:
            float(value)
            return 'floating-point number'
        except ValueError:
            return 'string'