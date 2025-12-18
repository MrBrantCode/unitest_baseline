"""
QUESTION:
Write a function named `prime_divisors` that generates a list of all prime divisors of a given number `n`, where `n` is the input parameter of the function. The function should return a list of prime divisors. Note that a prime divisor is a divisor that is also a prime number.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_divisors(n):
    divisors_list = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime(i):
            divisors_list.append(i)
        if n % i == 0 and is_prime(n // i) and n // i not in divisors_list and n // i != i:
            divisors_list.append(n // i)
    if n > 1 and is_prime(n):
        divisors_list.append(n)
    return divisors_list