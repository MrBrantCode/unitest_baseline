"""
QUESTION:
Compute the result based on the comparative size of x and y and the given formula. Implement a function `compute_result` that takes two integers x and y as input, and returns the result of the mathematical formula x^2 - 3y + 2 / (x^2 - y^2) if x is greater than y, otherwise y^2 - 3x + 2 / (y^2 - x^2). Ensure correct implementation of the mathematical formula and proper use of Python syntax for exponentiation and multiplication.
"""

def compute_result(x, y):
    if x > y:
        return x**2 - 3*y + 2 / (x**2 - y**2)
    else:
        return y**2 - 3*x + 2 / (y**2 - x**2)