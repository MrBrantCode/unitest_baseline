"""
QUESTION:
Design a function `find_primes_with_factors` that takes an integer `limit` as input, finds all prime numbers up to the given limit, and determines the sum of prime factors for each prime number found. The function should utilize the Sieve of Eratosthenes algorithm to efficiently generate prime numbers and return a list of all prime numbers found.
"""

import math

def find_primes_with_factors(limit):
    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(math.sqrt(n))+1):
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False

        return is_prime

    def find_prime_factors(num):
        prime_factors = []

        for i in range(2, int(math.sqrt(num))+1):
            while num % i == 0:
                prime_factors.append(i)
                num //= i

        if num > 1:
            prime_factors.append(num)

        return prime_factors

    is_prime = sieve_of_eratosthenes(limit)
    prime_numbers = []

    for i in range(2, limit+1):
        if is_prime[i]:
            prime_numbers.append(i)
            prime_factors = find_prime_factors(i)
            sum_of_factors = sum(prime_factors)
            print(f"The sum of prime factors for {i} is {sum_of_factors}")

    return prime_numbers