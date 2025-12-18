"""
QUESTION:
Write a function `find_emirps(n)` that generates the first N emirp numbers. An emirp number is a non-palindromic prime number whose reverse is also a prime number. The function should not include palindromic prime numbers in its output. Implement an efficient primality test in the function.
"""

import math

def find_emirps(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
              return False
        return True

    count = 0
    current = 2
    emirps = []
    while count < n:
        current_reversed = int(str(current)[::-1])

        if current != current_reversed and is_prime(current) and is_prime(current_reversed):
            emirps.append(current)
            count += 1

        current += 1
    return emirps