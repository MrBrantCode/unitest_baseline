"""
QUESTION:
Write a function that calculates the *least common multiple* of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return `1`.

~~~if:objc
NOTE: The first (and only named) argument of the function `n` specifies the number of arguments in the variable-argument list. Do **not** take `n` into account when computing the LCM of the numbers.
~~~
"""

from functools import reduce

def calculate_lcm(*args):
    """
    Calculate the least common multiple (LCM) of the provided non-negative integers.
    
    :param args: Variable-length argument list of non-negative integers.
    :return: The LCM of the provided integers. If no arguments are provided, returns 1.
    """
    if not args:
        return 1
    
    def gcd(a, b):
        """Helper function to calculate the greatest common divisor (GCD) of two numbers."""
        return b if a == 0 else gcd(b % a, a)
    
    def lcms(a, b):
        """Helper function to calculate the least common multiple (LCM) of two numbers."""
        return a * b // gcd(a, b)
    
    return reduce(lcms, args)