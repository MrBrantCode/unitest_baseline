"""
QUESTION:
Write a function named `digit_sum_product` that takes an integer as input, calculates the sum of its digits, and returns the product of the original number and the sum of its digits.
"""

def digit_sum_product(n):
    """
    This function calculates the sum of digits of the input number 
    and returns the product of the original number and the sum of its digits.

    Args:
        n (int): The input number.

    Returns:
        int: The product of the original number and the sum of its digits.
    """
    # Convert the number to a string to iterate over each digit
    return n * sum(int(digit) for digit in str(n))