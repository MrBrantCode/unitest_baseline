"""
QUESTION:
Implement the `sieve_of_eratosthenes(n)` function to return a list of all prime numbers up to a given number `n`. The function should use the Sieve of Eratosthenes algorithm and have a time complexity of O(n log log n). Do not use any built-in functions or libraries to solve this problem.
"""

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    i = 2
    while i*i <= n:
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
        i += 1

    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)

    return primes