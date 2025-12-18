"""
QUESTION:
Create a function `is_prime()` to check if a given number is prime and use this function to generate a sorted list of all prime numbers from 0 to 1000 using list comprehension. The `is_prime()` function should return `True` if a number is prime and `False` otherwise. The generated list should be in ascending order.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True