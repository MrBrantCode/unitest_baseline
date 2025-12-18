"""
QUESTION:
Create a function `prime_length` that takes a string as input, checks its length, and returns `True` if the length is a prime number, otherwise returns `False`. You can use an auxiliary function to validate whether a number is prime or not. The prime number check should work for any given positive integer.
"""

def prime_length(string):
    def _is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    return _is_prime(len(string))