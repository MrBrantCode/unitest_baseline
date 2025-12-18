"""
QUESTION:
Create a function `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. Using this function, create an array of integers ranging from -50 to 50, filter out the prime numbers, and print them in reverse order. Note that negative numbers can also be considered prime numbers in this context.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True