"""
QUESTION:
Write a function called `find_primes` that takes two parameters, `start` and `end`, and returns a list of all prime numbers between `start` and `end` (inclusive). The function should have a time complexity of O(n), where n is the difference between `start` and `end`, and should not use any built-in libraries or functions for checking prime numbers.
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