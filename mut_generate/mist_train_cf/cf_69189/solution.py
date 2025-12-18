"""
QUESTION:
Create a function called `check_prime(n)` that checks whether a given integer `n` is a prime number or not. Then, using a nested loop, traverse a 2D list of integers and identify the prime numbers. Include exception handling to catch any errors that may occur during this process. The function should take an integer as input and return a boolean value indicating whether the number is prime or not.
"""

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True