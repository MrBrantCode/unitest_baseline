"""
QUESTION:
Create a function called `calculate_elements` that takes two initial numbers as input, calculates the sum, difference, product, quotient, and remainder, and returns a list containing these five elements in that order. The quotient should be calculated using integer division (i.e., rounded down to the nearest whole number).
"""

def calculate_elements(num1, num2):
    """
    Calculate the sum, difference, product, quotient, and remainder of two numbers.
    
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
    
    Returns:
        list: A list containing the sum, difference, product, quotient, and remainder.
    """
    return [
        num1 + num2,  # sum
        num1 - num2,  # difference
        num1 * num2,  # product
        num1 // num2,  # quotient (integer division)
        num1 % num2  # remainder
    ]