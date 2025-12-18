"""
QUESTION:
Write a function called `validate_and_sum` that takes two arguments `num1` and `num2` and returns a list containing their sum if both numbers are positive integers greater than 10. If either `num1` or `num2` is not a positive integer greater than 10, the function should return an error message instead.
"""

def validate_and_sum(num1, num2):
    """
    Returns a list containing the sum of num1 and num2 if both numbers are positive integers greater than 10.
    Otherwise, returns an error message.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        list or str: A list containing the sum of num1 and num2, or an error message.
    """
    if num1 > 10 and num2 > 10 and isinstance(num1, int) and isinstance(num2, int):
        return [num1 + num2]
    else:
        return "Error: Both numbers should be positive integers greater than 10."