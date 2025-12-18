"""
QUESTION:
Create a function named `prime_divisors` that takes an integer `n` as input and returns a list of all prime numbers that are divisors of `n`. The function should consider the number itself as a potential prime divisor.
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
            if i != n // i and n % (n // i) == 0 and is_prime(n // i):
                divisors_list.append(n // i)
    if n > 1 and is_prime(n):
        divisors_list.append(n)
    return sorted(list(set(divisors_list)))