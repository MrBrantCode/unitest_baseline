"""
QUESTION:
Create a function `mersenne_number(n)` that determines if a given integer `n` is a Mersenne prime number, which is a prime number that can be written in the form `M_n = 2^n - 1` for some integer `n`. The function should return `True` if `n` is a Mersenne prime, and `False` otherwise. The function should be able to handle small inputs efficiently, but may not be required to handle very large inputs.
"""

import math

def mersenne_prime(n):
    """
    Determines if a given integer n is a Mersenne prime number.
    """
    def is_prime(num):
        """
        Determines if a number num is prime or not
        """
        if num == 2:
            return True
        if num % 2 == 0 or num <= 1:
            return False

        sqr = int(math.sqrt(num)) + 1

        for divisor in range(3, sqr, 2):
            if num % divisor == 0:
                return False
        return True

    supposed_power = math.log2(n+1)
    if supposed_power.is_integer():
        return is_prime(n)
    else:
        return False