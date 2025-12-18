"""
QUESTION:
Write a function `handleInput(x)` that takes an input `x` of any type and returns a string describing the type of input. The function should handle the following cases: null, positive integer, negative integer, zero, floating point number, and complex number. If the input type is not handled, the function should return "Unhandled input type". The function should also handle exceptions and return "Invalid input: (error details)" if an error occurs.
"""

def handleInput(x):
    try:
        if x is None:
            return "Input is null"
        elif isinstance(x, int):
            if x > 0:
                return "Positive integer"
            elif x < 0:
                return "Negative integer"
            else:
                return "Zero"
        elif isinstance(x, float):
            return "Floating point number"
        elif isinstance(x, complex):
            return "Complex number"
        else:
            return "Unhandled input type"
    except Exception as e:
        return f"Invalid input: {e}"