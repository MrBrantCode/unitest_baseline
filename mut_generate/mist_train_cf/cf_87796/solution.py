"""
QUESTION:
Write a function named `filter_primes` that takes a list of integers as input and returns a new list containing only the prime numbers. The function should use a lambda expression to filter out even numbers. Additionally, the solution should include a separate function named `is_prime` that checks if a number is prime or not, and this function should be used within the lambda expression for filtering.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(lambda x: is_prime(x) and x % 2 != 0, numbers))