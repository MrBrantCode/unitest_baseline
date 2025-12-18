"""
QUESTION:
Create a function `is_mersenne_prime` that takes an integer `n` as input. The function should return the power of 2, `p`, if `n` is a Mersenne prime (i.e., a prime number that is one less than a power of two, `n = 2^p - 1`) and `p` itself is a prime number. Otherwise, return a message indicating that `n` is not a Mersenne prime.
"""

from math import log2, sqrt

def is_prime(num):
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if (num % i == 0) or (num % (i + 2) == 0):
            return False
        i += 6

    return True

def is_mersenne_prime(n):
    log_result = log2(n + 1)

    if log_result.is_integer() and is_prime(log_result):
        return int(log_result)
    else:
        return "Not a Mersenne Prime"