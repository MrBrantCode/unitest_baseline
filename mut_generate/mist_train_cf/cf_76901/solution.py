"""
QUESTION:
Define a function named `penultimate_prime` that takes an array of integers as input and returns the second-to-last prime number in the array. The function should return `False` if the array contains fewer than two prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def penultimate_prime(arr):
    primes = []
    for i in reversed(arr):
        if is_prime(i):
            primes.append(i)
        if len(primes) == 2:
            return primes[1]
    return False