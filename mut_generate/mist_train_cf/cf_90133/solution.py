"""
QUESTION:
Write a function `sieve_of_eratosthenes` that generates a list of prime numbers between 10000 and 20000 and returns the sum of the first 100 prime numbers found. The function should use the Sieve of Eratosthenes algorithm and the input to the function should be the upper limit (20000) of the range of prime numbers.
"""

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False  

    p = 2
    while p**2 <= n:
        if is_prime[p]:
            for i in range(p**2, n+1, p):
                is_prime[i] = False
        p += 1

    primes = []
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)

    primes = [prime for prime in primes if prime >= 10000]
    return sum(primes[:100])