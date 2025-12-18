"""
QUESTION:
Write a function `is_prime` that checks if a number is prime. Using this function, print all prime numbers between 1 and 1000. The function should take an integer `num` as input and return a boolean value indicating whether the number is prime or not. The number is prime if it has exactly two distinct positive divisors: 1 and itself.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True