"""
QUESTION:
Write a function called `calculate` that takes three parameters: two numbers (`num1` and `num2`) and an operator (`operator`). The function should perform the operation specified by the operator on the two numbers and return the result. The operator can be '+', '-', '*', or '/'. If the operator is not one of these, the function should return an error message or handle it accordingly.
"""

def calculate(num1, num2, operator):
    """
    Perform the operation specified by the operator on the two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operator (str): The operator. Can be '+', '-', '*', or '/'.

    Returns:
        float: The result of the operation. Returns None for invalid operator.
    """
    if operator in ['+', '-', '*', '/']:
        return eval(f'{num1} {operator} {num2}')
    else:
        return None