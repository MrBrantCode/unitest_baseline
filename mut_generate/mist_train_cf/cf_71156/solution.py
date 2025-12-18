"""
QUESTION:
Design a function named `trailing_zeros` that calculates the number of trailing zeros in a given number's factorial. The function should take one argument `n`, an integer. The function should return the count of trailing zeros without calculating the factorial itself, considering that the number of trailing zeros in the factorial of a number n is determined by the number of factors of 5 in its prime factors.
"""

def trailing_zeros(n):
    """
    Calculate the number of trailing zeros in a given number's factorial.

    The function takes one argument `n`, an integer. It returns the count of 
    trailing zeros without calculating the factorial itself, considering that 
    the number of trailing zeros in the factorial of a number n is determined 
    by the number of factors of 5 in its prime factors.

    :param n: An integer
    :return: The count of trailing zeros
    """
    count = 0
    factor = 5
    while n >= factor:
        count += n // factor
        factor *= 5
    return count