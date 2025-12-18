"""
QUESTION:
Create a function called `perform_arithmetic_operation` that takes two numbers (`num1` and `num2`) and an arithmetic operation (`operation`) as input, and returns the result of the operation. The function should support the following operations: addition, subtraction, multiplication, and division. It should also handle division by zero by returning an error message. The input operation is guaranteed to be one of the four supported operations.
"""

def perform_arithmetic_operation(num1, num2, operation):
    """
    This function performs basic arithmetic operations on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The arithmetic operation to be performed.

    Returns:
        float or str: The result of the operation or an error message if division by zero is attempted.
    """

    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."