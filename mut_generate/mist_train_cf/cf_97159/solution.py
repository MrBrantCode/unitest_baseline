"""
QUESTION:
Write a function `count_digit_only_prime_divisors(n)` that takes an integer `n` and returns the total number of digit-only divisors of `n` that are also prime numbers. A digit-only divisor is defined as a divisor of `n` that only consists of the digits present in `n`. The function should be able to handle integers in the range `1 <= n <= 10^9`.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def count_digit_only_prime_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            str_i = str(i)
            if all(digit in str(n) for digit in str_i):
                if is_prime(i):
                    count += 1
            if i != n // i:
                str_divisor = str(n // i)
                if all(digit in str(n) for digit in str_divisor):
                    if is_prime(n // i):
                        count += 1
    return count