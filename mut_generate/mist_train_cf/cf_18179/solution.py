"""
QUESTION:
Create a program with a function named calculate(num1, num2, operator) that takes two numbers and an operator as input and returns the result of the operation. The numbers should be within the range of -1000 to 1000 and the operator should be one of '+', '-', '*', '/'. The function should also handle division by zero by returning an error message instead of throwing an exception.
"""

def calculate(num1, num2, operator):
    """
    Performs a mathematical operation on two numbers based on the provided operator.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        operator (str): The operator to apply (+, -, *, /).

    Returns:
        int or float: The result of the operation, or an error message if division by zero is attempted.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."