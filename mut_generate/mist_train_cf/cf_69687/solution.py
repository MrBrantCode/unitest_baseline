"""
QUESTION:
Create a function called `foo` that takes three parameters `a`, `b`, and `d` of type `int` or `float`, adds them together, and returns the result. The function should handle exceptions and return an appropriate error message if the parameters are not of the correct type or if an error occurs during the operation.
"""

def entrance(a, b, d):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(d, (int, float)):
            c = a + b + d
        else:
            return "One or more parameters are not of type int or float"
    except Exception as e:
        return str(e)
    return c