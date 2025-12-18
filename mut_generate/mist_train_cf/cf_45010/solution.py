"""
QUESTION:
Write a function `is_prime(num)` that takes an integer `num` as input and returns `True` if it's a prime number (divisible by 1 and itself only) and `False` otherwise. Assume the input number is a positive integer. The function should be efficient for large numbers by only checking divisors up to the square root of `num`.
"""

def is_prime(num):
    """Return True if the number is prime, False otherwise"""
    # If the number is less than 2, it is not prime
    if num < 2:
        return False
    # Check each number up to the square root of num to see if it is a divisor
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True