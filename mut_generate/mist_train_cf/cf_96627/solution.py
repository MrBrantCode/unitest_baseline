"""
QUESTION:
Write a function named `odd_prime_numbers` that takes a list of integers as input and returns a new list containing only the odd prime numbers from the input list. Use the built-in `filter()` function and define a helper function to check if a number is prime. The function should not include any input validation or error handling, and the input list is assumed to contain only integers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def odd_prime_numbers(lst):
    return list(filter(lambda x: is_prime(x) and x % 2 != 0, lst))