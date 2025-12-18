"""
QUESTION:
Write a function `find_primes(start, end)` that takes in two parameters, `start` and `end`, and returns a list of all the prime numbers between `start` and `end` (inclusive) using a for loop. The function should not use any built-in libraries or functions for checking prime numbers and should have an optimized algorithm to improve the efficiency of prime number checking.
"""

def find_primes(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes