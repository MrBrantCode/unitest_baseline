"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given number without using the multiplication operator or any built-in factorial functions. The function should take an integer `num` as input and return its factorial. The factorial should be calculated using a for loop.
"""

def factorial(num):
    """
    Calculate the factorial of a given number without using the multiplication operator.
    
    Args:
    num (int): The number for which the factorial is to be calculated.
    
    Returns:
    int: The factorial of the given number.
    """
    result = 1
    for i in range(1, num + 1):
        result = result + result * (i - 1)
    return result