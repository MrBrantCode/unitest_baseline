"""
QUESTION:
Write a function called "math_description" that takes two numbers as input and a mathematical operation. The function should return a string describing the relationship between the two numbers in terms of the operation. The operation is multiplication.
"""

def math_description(num1, num2):
    """
    This function takes two numbers as input and returns a string describing their relationship in terms of multiplication.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        str: A string describing the relationship between the two numbers in terms of multiplication.
    """

    if num1 % num2 == 0:
        multiplier = num1 // num2
        return f"{num1} is {multiplier} times the amount of {num2}."
    elif num2 % num1 == 0:
        multiplier = num2 // num1
        return f"{num2} is {multiplier} times the amount of {num1}."
    else:
        return "There is no whole number relationship between the two numbers in terms of multiplication."