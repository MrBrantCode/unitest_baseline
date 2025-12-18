"""
QUESTION:
Create a function named `multiply_three_numbers` that takes three integers as input and returns their product. If at least two of the inputs are zero, return the string "Invalid input. Please input at least two non-zero integers." The function should be able to handle large integers without causing a memory error.
"""

def multiply_three_numbers(a, b, c):
    """
    This function takes three integers as input and returns their product.
    If at least two of the inputs are zero, it returns an error message.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        int or str: The product of the three integers, or an error message if at least two inputs are zero.
    """
    # Check if two or more inputs are zero
    if (a == 0 and b == 0) or (b == 0 and c == 0) or (c == 0 and a == 0):
        return "Invalid input. Please input at least two non-zero integers."
    else:
        return a * b * c