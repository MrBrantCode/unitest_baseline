"""
QUESTION:
Create a function called `generate_primes` that takes an integer `n` and returns a list of the first `n` prime numbers. The function should not use external libraries or functions for prime number generation, and should not use iterative or recursive methods for checking primality such as trial division or the Sieve of Eratosthenes. The time complexity of the function should be O(n^2) or better. Handle edge cases where `n` is 0 or negative.
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