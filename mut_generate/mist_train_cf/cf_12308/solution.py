"""
QUESTION:
Write a function `filter_primes` that takes a list of integers as input and returns a new list containing only the prime numbers greater than 2 from the original list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should not modify the original list.
"""

def filter_primes(arr):
    return [num for num in arr if num > 2 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]