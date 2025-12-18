"""
QUESTION:
Implement a function `is_prime(num)` that checks if a given number is prime. Use this function to print all prime numbers between 1 and 1000. The function should return `False` for numbers less than 2 and `True` if the number has no divisors other than 1 and itself. The iteration to check for divisors should only go up to the square root of the number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True