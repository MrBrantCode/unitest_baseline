"""
QUESTION:
Create a function called `calculate` that takes a string representing a simple arithmetic expression as input and returns the result of that expression. The function should be able to handle basic arithmetic operators such as addition, subtraction, multiplication, and division. The input string will only contain non-negative integers, arithmetic operators, and spaces.
"""

def calculate(expression):
    """
    This function calculates a simple arithmetic expression.

    Args:
        expression (str): A string representing a simple arithmetic expression.

    Returns:
        result: The result of the arithmetic expression.
    """
    return eval(expression)