"""
QUESTION:
Write a function `generate_primes(n)` to generate an array containing prime numbers between 1 and `n`, with a time complexity of O(n) and space complexity of O(n).
"""

def generate_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p*p <= n:
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
        p += 1

    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)

    return primes