"""
QUESTION:
Write a function called `find_prime_info` that takes an integer as input and returns a tuple. The tuple should contain a boolean indicating whether the input number is prime, a list of the next two prime numbers if the input is not prime, and a list of prime factors of the input number if it is not prime. The function should only consider positive integers and should be efficient for large inputs.
"""

import math

def find_prime_info(num):
    if num < 2:
        return (False, [], [])

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def find_next_primes(n, count):
        primes = []
        while len(primes) < count:
            n += 1
            if is_prime(n):
                primes.append(n)
        return primes

    def find_prime_factors(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n = n // i
        if n > 2:
            factors.append(n)
        return factors

    if is_prime(num):
        return (True, [], [])
    else:
        next_primes = find_next_primes(num, 2)
        prime_factors = find_prime_factors(num)
        return (False, next_primes, prime_factors)