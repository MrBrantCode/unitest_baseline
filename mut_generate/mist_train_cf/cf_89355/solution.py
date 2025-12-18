"""
QUESTION:
Write a function `find_primes` that takes two integers `start` and `end` as input and prints all prime numbers within the given range, excluding numbers divisible by any prime number within the range. The function should have a time complexity of O(n*log(log(n))), where n is the upper limit of the range, and should not use any external libraries or pre-built functions to check for prime numbers.
"""

import math

def find_primes(start, end):
    """Find all prime numbers within a given range."""
    primes = [2]  # Start with 2 as the only prime number

    def is_prime(num):
        """Check if a number is prime based on a list of primes."""
        sqrt_num = int(math.sqrt(num))
        for prime in primes:
            if prime > sqrt_num:
                break
            if num % prime == 0:
                return False
        return True

    for num in range(start, end+1):
        if is_prime(num) and all(num % p != 0 for p in primes if p != num):
            primes.append(num)
            print(num, end=' ')