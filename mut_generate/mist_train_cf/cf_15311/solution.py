"""
QUESTION:
Create a function named `get_primes` that takes an integer `n` as input and returns a list containing the first `n` prime numbers. The function should not use external libraries, iterative or recursive methods for prime number generation, or the Sieve of Eratosthenes. Implement a more advanced primality testing algorithm. Handle edge cases such as `n = 0` or negative values. The time complexity should be O(n^2) or better.
"""

def get_primes(n):
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

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes