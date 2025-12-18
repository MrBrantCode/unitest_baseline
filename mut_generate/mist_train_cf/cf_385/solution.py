"""
QUESTION:
Implement a function called `generate_primes` in Python that generates an array of prime numbers from 0 to 100 in descending order using a recursive function and the Sieve of Eratosthenes algorithm. The function should have a time complexity of O(n√n).
"""

def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def generate_primes(n=100):
    if n < 2:
        return []
    primes = generate_primes(n - 1)
    if is_prime(n):
        primes.append(n)
    return primes[::-1]