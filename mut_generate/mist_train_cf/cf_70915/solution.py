"""
QUESTION:
Write a function named `multiply_values` that takes an integer and a string representing a number, and returns the result of multiplying the integer by the numerical value of the string. The function should handle type conversion to ensure the correct result.
"""

def multiply_values(num1, num2):
    """
    This function multiplies an integer by the numerical value of a string.
    
    Args:
    num1 (int): The integer to multiply.
    num2 (str): The string representing a number to be multiplied by num1.
    
    Returns:
    int: The result of multiplying num1 by the numerical value of num2.
    """
    return num1 * int(num2)