"""
QUESTION:
Write a function `is_prime` that checks if a given number is prime, and use this function to print all prime numbers between 1 and 1000. The function should consider a prime number as a whole number greater than 1 that is divisible by only 1 and itself. It should be optimized to only check divisibility up to the square root of the number. Additionally, it should only check odd numbers greater than 2, as even numbers greater than 2 cannot be prime.
"""

import math

def entrance(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True