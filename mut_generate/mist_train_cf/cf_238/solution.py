"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. The function should use the Sieve of Eratosthenes algorithm and should be able to handle large input numbers up to 10^9 efficiently, with a time complexity less than O(n). Do not use any built-in library functions or external libraries for determining prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False

    prime = [True for _ in range(n+1)]
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    return prime[n]