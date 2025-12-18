"""
QUESTION:
Create a function named `sieve_of_eratosthenes` that takes a positive integer `n` greater than 2 as input. The function should use the Sieve of Eratosthenes algorithm to generate a list of prime numbers between 2 and `n`, and return a dictionary containing these prime numbers as keys with their corresponding prime factors as values, as well as the sum of all prime numbers generated.
"""

def entrance(n):
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
            factors[p] = []

    for p in primes:
        for i in range(2, p):
            if p % i == 0:
                factors[p].append(i)

    prime_sum = sum(primes)

    return primes, factors, prime_sum