"""
QUESTION:
Create a function `sieve_of_eratosthenes` that uses the Sieve of Eratosthenes algorithm to find the first n prime numbers. The function should return a list of the first n prime numbers. Note that the function should be able to find the first n prime numbers, not just the prime numbers up to n.
"""

def first_n_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    primes = []

    while count < n:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1

    return primes