"""
QUESTION:
Write a function named `is_prime(num)` that checks whether a given number is prime. A prime number is only divisible by 1 and itself. Then, use this function to print all numbers between 0 and 100 that are divisible by both 3 and 5, and are also prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True