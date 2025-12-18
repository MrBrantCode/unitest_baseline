"""
QUESTION:
Write three functions, `is_prime(n)`, `is_perfect_square(n)`, and `is_palindrome(n)`, that take a positive integer `n` as input and return `True` if the number is a prime number, a perfect square, and a palindrome, respectively, and `False` otherwise. Assume that the input number `n` is a positive integer greater than 0.
"""

import math

def entrance(n):
    def is_prime():
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect_square():
        square_root = math.isqrt(n)
        return square_root * square_root == n

    def is_palindrome():
        number_str = str(n)
        return number_str == number_str[::-1]

    return is_prime(), is_perfect_square(), is_palindrome()