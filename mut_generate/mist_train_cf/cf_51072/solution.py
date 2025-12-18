"""
QUESTION:
Create a function `is_prime` that takes an integer as input and returns a boolean indicating whether the number is prime. Then, using the `is_prime` function, find the first 20 prime numbers and calculate their average. Do not use any libraries or built-in functions for prime number generation or calculation. The output should include the list of the first 20 prime numbers and their average.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True