"""
QUESTION:
Create a function `get_primes(n)` that takes in a non-negative integer `n` and returns a list containing the first `n` prime numbers. The function should implement a primality testing algorithm with a time complexity of O(n^2) or better without using external libraries or functions, iterative or recursive methods for checking primality, or trial division.
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