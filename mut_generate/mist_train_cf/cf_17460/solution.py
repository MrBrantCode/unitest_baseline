"""
QUESTION:
Write a function `divideTwoNumbers` that takes two parameters `a` and `b`. The function should return the result of `a` divided by `b` while considering the following conditions:

- If `a` and `b` are both integers, the result should be an integer.
- If either `a` or `b` is a floating-point number, the result should be a floating-point number.
- If `a` or `b` is a non-numeric value, the function should return "Invalid input! Please provide numeric values."
- If `b` is 0, the function should return "Division by 0 not allowed!"

There are no restrictions on the function's implementation.
"""

def divide_two_numbers(a, b):
    """
    Divide two numbers while considering integer and float division.

    Args:
    a (int or float): The dividend.
    b (int or float): The divisor.

    Returns:
    int or float: The result of the division, or an error message if the input is invalid.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid input! Please provide numeric values."
    
    if b == 0:
        return "Division by 0 not allowed!"
    
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    
    return a / b