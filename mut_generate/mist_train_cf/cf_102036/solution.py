"""
QUESTION:
Implement a function named `add` that takes two parameters, `num1` and `num2`, and returns their sum if both are integers. The function should also handle cases where the inputs are not integers.
"""

def add(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    else:
        return "Both inputs must be integers."