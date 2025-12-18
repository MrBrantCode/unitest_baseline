"""
QUESTION:
Create a function `check_divisibility` that takes an integer `n` as input and returns a string based on the divisibility of `n` by 4 and 7. The function should return "Even and Divisible by 7" if `n` is divisible by both 4 and 7, "Even" if `n` is divisible by 4 but not 7, "Divisible by 7" if `n` is divisible by 7 but not 4, and "Odd" otherwise. The input `n` is between 1 and 20.
"""

def check_divisibility(n):
    """
    This function checks the divisibility of a number by 4 and 7.
    
    Args:
        n (int): The input number to be checked.
    
    Returns:
        str: A string based on the divisibility of n by 4 and 7.
    """
    if n % 4 == 0 and n % 7 == 0:
        return "Even and Divisible by 7"
    elif n % 4 == 0:
        return "Even"
    elif n % 7 == 0:
        return "Divisible by 7"
    else:
        return "Odd"