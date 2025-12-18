"""
QUESTION:
Write a function named `get_primes` that takes an integer `n` as input and returns the first `n` prime numbers in ascending order. Then, using this function, print the 10th and 11th prime numbers and check if they are consecutive, printing a message stating whether they are consecutive or not. The function should use a helper function `is_prime` to check if a number is prime.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes