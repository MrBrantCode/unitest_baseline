"""
QUESTION:
Create a function named `sum_proper_divisors` that takes a positive integer `num` and returns the sum of all its proper divisors excluding any divisors that are prime numbers. The function should have a time complexity of O(sqrt(n)) and a space complexity of O(1).
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_proper_divisors(num):
    sum_divisors = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if i != num and not is_prime(i):
                sum_divisors += i
            if i != num and i != num // i and not is_prime(num // i):
                sum_divisors += num // i
    return sum_divisors