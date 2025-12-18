"""
QUESTION:
Write a function `display_multiplication_table(n)` that prints the multiplication table of a given number `n`, but only displays the multiplication results for prime numbers less than or equal to `n`. Implement a helper function `is_prime(num)` to check whether a given number `num` is prime. The `is_prime(num)` function should iterate up to the square root of `num` for efficiency.
"""

import math

def display_multiplication_table(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(2, n+1) if is_prime(i)]
    for prime in primes:
        row = [prime * i for i in range(1, n+1)]
        print(row)