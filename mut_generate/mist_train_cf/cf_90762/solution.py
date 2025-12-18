"""
QUESTION:
Write a function called `generate_prime_array` that generates an array of prime numbers up to and including the input number `n`. The function should return a list of integers. The input `n` is a positive integer.
"""

def generate_prime_array(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes