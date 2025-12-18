"""
QUESTION:
Create a function `is_prime(num)` that takes a positive integer `num` as input and returns a boolean value indicating whether `num` is a prime number. The input `num` must be within the range of 2 to 10^9, inclusive.
"""

def is_prime(num):
    if num < 2 or num > 10**9:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True