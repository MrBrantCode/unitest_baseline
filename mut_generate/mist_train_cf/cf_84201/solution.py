"""
QUESTION:
Create a function called `calculate_arithmetic_operations` that takes two numerical inputs and returns their addition, subtraction, multiplication, and division results. The function should be able to handle division by non-zero numbers.
"""

def calculate_arithmetic_operations(num1, num2):
    """
    This function calculates the addition, subtraction, multiplication, and division of two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        tuple: A tuple containing the results of addition, subtraction, multiplication, and division.
    """
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Error: Division by zero is not allowed"

    return addition, subtraction, multiplication, division