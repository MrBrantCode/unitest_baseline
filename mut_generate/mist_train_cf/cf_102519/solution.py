"""
QUESTION:
Write a function named `add_numbers` that takes two arguments, `num1` of type int and `num2` of type float, and returns their sum as a float, demonstrating the implicit conversion of the int value to a float value during the addition operation.
"""

def add_numbers(num1: int, num2: float) -> float:
    """
    Adds two numbers, an integer and a float, and returns their sum as a float.
    
    The int value is implicitly converted to a float value during the addition operation.
    
    Args:
    num1 (int): The integer to be added.
    num2 (float): The float to be added.
    
    Returns:
    float: The sum of num1 and num2 as a float.
    """
    return num1 + num2