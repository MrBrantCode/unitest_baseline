"""
QUESTION:
Write a function `is_prime(num)` that checks if a number `num` is prime, then use it to calculate the sum of the first 100 prime numbers between 1 and 2000, inclusive. The function `is_prime(num)` should return `True` if `num` is prime and `False` otherwise.
"""

def is_prime(num):
    """
    This function checks if a number is prime or not.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True