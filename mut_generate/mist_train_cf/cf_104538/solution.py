"""
QUESTION:
Write a function named `modulo_and_divisibility` that takes two integers as input and returns the modulo of the two numbers. The function should also print a message indicating whether the first number is divisible by the second number. The input integers are between 1 and 1000 inclusive.
"""

def modulo_and_divisibility(num1, num2):
    """
    Calculate the modulo of two numbers and check if the first number is divisible by the second number.

    Args:
        num1 (int): The dividend.
        num2 (int): The divisor.

    Returns:
        int: The modulo of num1 and num2.
    """
    modulo = num1 % num2
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}")
    else:
        print(f"{num1} is not divisible by {num2}")
    return modulo