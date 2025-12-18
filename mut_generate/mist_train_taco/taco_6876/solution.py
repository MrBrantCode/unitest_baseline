"""
QUESTION:
In this Kata, you will implement a function `count` that takes an integer and returns the number of digits in `factorial(n)`. 

For example, `count(5) = 3`, because `5! = 120`, and `120` has `3` digits.  

More examples in the test cases. 

Brute force is not possible. A little research will go a long way, as this is a well known series.

Good luck!

Please also try:
"""

from math import ceil, lgamma, log

def count_digits_in_factorial(n: int) -> int:
    """
    Calculate the number of digits in the factorial of a given integer n.

    Parameters:
    n (int): The integer for which to calculate the factorial and count its digits.

    Returns:
    int: The number of digits in the factorial of n.
    """
    return ceil(lgamma(n + 1) / log(10))