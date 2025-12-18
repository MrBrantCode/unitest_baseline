"""
QUESTION:
Create a function `check_divisibility` that takes an integer `n` as input and returns `True` if `n` is divisible by both 3 and 5, as well as by 7, without using the modulus operator.
"""

def check_divisibility(n):
    """
    Checks if a number is divisible by both 3 and 5, as well as by 7.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is divisible by both 3 and 5, as well as by 7, False otherwise.
    """
    temp = n
    while temp >= 3:
        temp -= 3
    div3 = temp == 0

    temp = n
    while temp >= 5:
        temp -= 5
    div5 = temp == 0

    temp = n
    while temp >= 7:
        temp -= 7
    div7 = temp == 0

    return div3 and div5 and div7