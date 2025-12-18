"""
QUESTION:
Write a function `compare_numbers` that takes two integers `num1` and `num2` as input and returns a string indicating whether `num1` is smaller, greater, or equal to `num2`, and also whether `num1` is divisible by `num2`. The function should handle division by zero errors by not considering `num1` to be divisible by `num2` if `num2` is zero.
"""

def compare_numbers(num1, num2):
    """
    Compare two integers and determine whether the first number is smaller, 
    greater, or equal to the second number, and also whether the first number 
    is divisible by the second number.

    Args:
    num1 (int): The first integer.
    num2 (int): The second integer.

    Returns:
    str: A string indicating the comparison result and divisibility.
    """
    if num1 < num2:
        return f"{num1} is smaller than {num2}"
    elif num1 > num2:
        return f"{num1} is greater than {num2}"
    else:
        if num2 == 0:
            return f"{num1} is equal to {num2} but cannot be divisible by zero"
        elif num1 % num2 == 0:
            return f"{num1} is equal to {num2} and is divisible by {num2}"
        else:
            return f"{num1} is equal to {num2} but is not divisible by {num2}"