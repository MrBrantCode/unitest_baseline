"""
QUESTION:
Create a function called `subtract_numbers` that takes two integers as input, ensuring the first number is greater than or equal to the second number. If the first number is not greater, the function should swap the numbers. The function should calculate the absolute difference between the two numbers without using built-in absolute value functions or methods and return the result.
"""

def subtract_numbers(num1, num2):
    """
    Calculate the absolute difference between two numbers, ensuring the first number is greater than or equal to the second number.
    
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
    
    Returns:
        int: The absolute difference between num1 and num2.
    """

    # Swap the numbers if the first number is smaller than the second number
    if num1 < num2:
        num1, num2 = num2, num1

    # Calculate the difference between the two numbers
    difference = num1 - num2

    # Calculate the absolute value of the difference without using built-in functions
    if difference < 0:
        difference *= -1

    return difference