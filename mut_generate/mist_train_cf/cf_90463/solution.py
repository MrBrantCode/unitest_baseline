"""
QUESTION:
Write a function named `find_second_smallest_prime` that takes a list of integers as input and returns the second smallest prime number in the list without using any loops or recursion. If there are less than two prime numbers in the list, the function should return None.
"""

def find_second_smallest_prime(numbers):
    primes = sorted(filter(lambda n: all(n % i != 0 for i in range(2, int(n**0.5) + 1)) and n > 1, numbers))
    return primes[1] if len(primes) > 1 else None