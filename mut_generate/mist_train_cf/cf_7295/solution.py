"""
QUESTION:
Write a Python function named `find_largest_prime` that takes two integers `start` and `end` representing a range, and returns the largest prime number within that range. The function should use a lambda expression and a filter function to check if a number is prime.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_largest_prime(start, end):
    primes = filter(lambda x: is_prime(x), range(start, end+1))
    largest_prime = max(primes)
    return largest_prime