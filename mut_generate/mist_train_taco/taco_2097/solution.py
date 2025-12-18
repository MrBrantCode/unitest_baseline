"""
QUESTION:
An abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself. 

The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).

Derive function `abundantNumber(num)/abundant_number(num)` which returns `true/True/.true.` if `num` is abundant, `false/False/.false.` if not.
"""

def is_abundant(num):
    """
    Check if a given number is an abundant number.

    An abundant number is a number for which the sum of its proper divisors 
    is greater than the number itself.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the number is abundant, False otherwise.
    """
    return sum([e for e in range(1, num) if num % e == 0]) > num