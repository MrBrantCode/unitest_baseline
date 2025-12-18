"""
QUESTION:
Create a function `SieveOfEratosthenes(n)` to generate all prime numbers up to `n` using the Sieve of Eratosthenes algorithm. The function should have a space complexity of O(n). Additionally, create another function `get_first_n_primes(n)` that uses `SieveOfEratosthenes(n)` to return the first `n` prime numbers, with the ability to efficiently handle primes up to one million.
"""

def SieveOfEratosthenes(n):
    is_prime = [False] * (n+1)
    p = 2
    while p * p <= n:
        if is_prime[p] == False:
            for i in range(p * p, n+1, p):
                is_prime[i] = True
        p += 1

    prime_list = []

    for p in range(2, n):
        if is_prime[p] == False:
            prime_list.append(p)
    return prime_list


def get_first_n_primes(n):
    primes = SieveOfEratosthenes(10**6)  # generate primes up to one million
    return primes[:n]