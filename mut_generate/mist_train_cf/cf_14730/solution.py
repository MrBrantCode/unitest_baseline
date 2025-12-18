"""
QUESTION:
Write a function `find_prime_numbers` that takes two integers `start` and `end` as input and returns a list of all prime numbers between `start` and `end` (inclusive). The function should not take any other inputs. The function should only consider integers and should not include `start` or `end` in the output if they are not prime numbers.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start + 1, end):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers