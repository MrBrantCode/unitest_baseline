"""
QUESTION:
Write a function `generate_primes(n)` that takes an integer `n` as input and returns a list of all prime numbers from 0 to `n`. Implement the solution from scratch without using any built-in functions or libraries for prime number generation. The function should have a time complexity of O(n√n) or better.
"""

def generate_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)

    return primes