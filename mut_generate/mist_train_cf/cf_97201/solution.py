"""
QUESTION:
Write a function called `is_prime(n)` that checks if a number is prime and then use it to print a multiplication table of a given size (in this case 15), only including the prime numbers in the table. The function should take an integer `n` as input and return a boolean value indicating whether the number is prime. The multiplication table should be printed with prime numbers aligned in a grid and non-prime numbers replaced with empty spaces.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True