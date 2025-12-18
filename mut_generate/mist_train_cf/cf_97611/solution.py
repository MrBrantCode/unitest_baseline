"""
QUESTION:
Write a function named `division_with_remainder` that takes two integer arguments, `num1` and `num2`, and returns the result of dividing `num1` by `num2` while also printing the remainder of the division.
"""

def division_with_remainder(num1, num2):
    """
    This function takes two integer arguments and returns the result of dividing the first by the second
    while also printing the remainder of the division.
    
    Parameters:
    num1 (int): The dividend.
    num2 (int): The divisor.
    
    Returns:
    int: The quotient of num1 divided by num2.
    """
    quotient = num1 // num2 # integer division
    remainder = num1 % num2 # remainder
    print(f"{num1} divided by {num2} is {quotient} with a remainder of {remainder}")
    return quotient