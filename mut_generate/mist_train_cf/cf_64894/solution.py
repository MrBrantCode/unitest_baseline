"""
QUESTION:
Create a function that takes a list of integers as input and returns a generator expression that yields only the prime numbers from the list. The function should use a helper function to check if a number is prime. Implement the solution using a generator expression and exclude any irrelevant code snippets. The input list contains integers, and the function should only return prime numbers.
"""

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    """Generator expression to get prime numbers from a list"""
    return (i for i in numbers if is_prime(i))