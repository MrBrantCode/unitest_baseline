"""
QUESTION:
Create a function `evaluate_expression(a, b, c)` that calculates the result of the mathematical expression `a * (b + c)`. The function should accept three positive integer parameters `a`, `b`, and `c` with values ranging from 1 to 100, and return the result of the expression. If any of the input values is outside the valid range, the function should return an error message.
"""

def evaluate_expression(a, b, c):
    if a < 1 or a > 100 or b < 1 or b > 100 or c < 1 or c > 100:
        return "Invalid input. All values must be between 1 and 100."

    result = a * (b + c)
    return result