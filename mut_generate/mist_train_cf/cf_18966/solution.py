"""
QUESTION:
Write a function `sum_bitwise()` that takes two integers from the user as input and returns their sum using only bitwise operations (i.e., no arithmetic operators or loops are allowed).
"""

def sum_bitwise(a, b):
    """
    This function calculates the sum of two numbers using only bitwise operations.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of a and b.
    """
    # Iterate until there are no more carry bits
    while b != 0:
        # Calculate the carry bit
        carry = a & b

        # Calculate the sum without carry
        a = a ^ b

        # Left shift the carry by 1 bit
        b = carry << 1

    # Return the sum
    return a