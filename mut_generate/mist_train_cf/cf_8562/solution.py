"""
QUESTION:
Write a function named `find_second_smallest_prime` that takes a list of integers as input and returns the second smallest prime number in the list without using any loops or recursion. The function should return `None` if the list has less than two prime numbers.
"""

def find_second_smallest_prime(numbers):
    primes = sorted([n for n in numbers if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))])
    return primes[1] if len(primes) > 1 else None