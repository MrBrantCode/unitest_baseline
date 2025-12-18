"""
QUESTION:
Create a function `calculate_result` that takes two integers as input and performs a series of mathematical operations in the following order: subtract the second number from the first, multiply the result by 5, divide the result by 2, and add 10 to the result. The function should return the final result.
"""

def calculate_result(first_number, second_number):
    """
    This function takes two integers as input and performs a series of mathematical operations.
    
    The operations are performed in the following order: 
    - Subtract the second number from the first, 
    - Multiply the result by 5, 
    - Divide the result by 2, 
    - Add 10 to the result.

    Args:
    first_number (int): The first number
    second_number (int): The second number

    Returns:
    float: The final result
    """
    return ((first_number - second_number) * 5) / 2 + 10