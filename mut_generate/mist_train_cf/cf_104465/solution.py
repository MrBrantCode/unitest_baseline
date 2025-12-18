"""
QUESTION:
Implement a function called `perform_arithmetic_operation` that takes two numbers and an arithmetic operation as input, performs the specified operation, and returns the result. The function should handle division by zero and invalid input. It should also provide an option to perform multiple arithmetic operations in a single run without terminating the program after each operation.
"""

import math

def perform_arithmetic_operation(number1, number2, operation):
    """
    This function performs arithmetic operations and returns the result.

    Args:
    number1 (float): The first number.
    number2 (float): The second number.
    operation (str): The arithmetic operation to be performed.

    Returns:
    float: The result of the operation.
    """
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '/':
        try:
            return number1 / number2
        except ZeroDivisionError:
            return "Error: Division by zero"
    elif operation == '*':
        return number1 * number2
    elif operation == 'sin':
        return math.sin(number1)
    elif operation == 'cos':
        return math.cos(number1)
    elif operation == 'log':
        return math.log(number1)