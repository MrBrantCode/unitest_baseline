"""
QUESTION:
Create a function called `primes_up_to_n` that takes a positive integer `n` as input and returns an array of all the prime numbers up to `n`. The function should have a time complexity of O(n^2), handle edge cases where `n` is 0 or 1, and not use any external libraries or built-in functions to check for prime numbers. It should utilize the Sieve of Eratosthenes algorithm to determine prime numbers, and implement helper functions to check if a number is prime using trial division and generate all possible prime factors of a number.
"""

def primes_up_to_n(n):
    if n <= 1:
        return []

    # Helper function to check if a number is prime using trial division
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes