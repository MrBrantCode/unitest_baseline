"""
QUESTION:
Write a function to compute the product of num1 divided by num2. The function should take two parameters: num1 and num2, which are positive integers between 1 and 1000 (inclusive). The result should be rounded to the nearest whole number and returned. The function should also check if the result is divisible by both num1 and num2 without a remainder and return a boolean value indicating this condition.
"""

def divide_and_check(num1, num2):
    """
    Compute the product of num1 divided by num2, round the result to the nearest whole number,
    and check if the result is divisible by both num1 and num2.

    Parameters:
    num1 (int): A positive integer between 1 and 1000 (inclusive).
    num2 (int): A positive integer between 1 and 1000 (inclusive).

    Returns:
    tuple: A tuple containing the rounded result and a boolean indicating if the result is divisible by both num1 and num2.
    """

    result = round(num1 / num2)
    divisible = result % num1 == 0 and result % num2 == 0
    return result, divisible