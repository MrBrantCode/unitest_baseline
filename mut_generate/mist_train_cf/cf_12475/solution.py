"""
QUESTION:
Write a function named `is_prime` to determine if a given number is prime, and use it to print all prime numbers in a range from `start` to `end` where `start` is greater than 1 and `end` is less than or equal to 10^6.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True