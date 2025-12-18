"""
QUESTION:
Write a function called `bitwise_addition` that takes two positive integers less than 100 as input and returns their sum without using the addition operator or any mathematical operators. The function should also ensure that the input integers are prime numbers.
"""

def bitwise_addition(a, b):
    """
    This function performs bitwise addition of two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of a and b.
    """
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a