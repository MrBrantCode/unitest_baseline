"""
QUESTION:
Create a function named `is_prime()` to determine whether a number is prime. Then, design a main function to find all numbers between 0 and 100 inclusive that are divisible by both 3 and 5, and also prime. The main function should print these numbers and return the sum of the prime numbers found.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True