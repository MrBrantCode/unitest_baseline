"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that generates a list of prime numbers between 2 and n (where n is a positive integer greater than 2) using the Sieve of Eratosthenes algorithm. The function should return a list of prime numbers, a dictionary where the keys are the prime numbers and the values are lists of their corresponding factors, and the sum of all prime numbers.
"""

def sieve_of_eratosthenes(n):
    primes = []
    factors = {}
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5)+1):
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False

    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            factors[p] = [i for i in range(2, p) if p % i == 0]

    prime_sum = sum(primes)

    return primes, factors, prime_sum