"""
QUESTION:
Find all Armstrong numbers within a given range. An Armstrong number is a number such that the sum of its digits raised to the third power is equal to the number itself. Write a function named 'isArmstrong' to identify whether a given number is an Armstrong number or not. The function should take an integer 'num' as input and return True if 'num' is an Armstrong number, False otherwise.
"""

def isArmstrong(num):
    """
    Checks if a given number is an Armstrong number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    s = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        s += digit ** 3
        temp //= 10
    return num == s