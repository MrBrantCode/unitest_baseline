"""
QUESTION:
Implement a function called `generate_primes` that takes an integer `n` as input and returns a list of the first `n` prime numbers. The function should have a time complexity of O(n^2) or better, and should not use any external libraries or functions for prime number generation. The function should also handle edge cases such as `n = 0` or negative values.
"""

def generate_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    if n <= 0:
        return []
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes