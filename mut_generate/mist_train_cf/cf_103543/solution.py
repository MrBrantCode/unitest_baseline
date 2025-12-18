"""
QUESTION:
Create a function that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should utilize list comprehension and a helper function to check for primality.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    return [num for num in numbers if is_prime(num)]