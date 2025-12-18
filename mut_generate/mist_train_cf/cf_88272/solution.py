"""
QUESTION:
Create a function `is_prime()` that checks if a given number is prime and use this function in a list comprehension to generate a list of all prime numbers from 0 to 1000, then sort the list in ascending order. The list comprehension should filter out non-prime numbers using the `is_prime()` function. The function `is_prime()` should return a boolean value, and the list comprehension should return a sorted list of integers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True