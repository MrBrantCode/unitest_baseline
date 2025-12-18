"""
QUESTION:
Write a function called `is_prime(num)` that takes an integer as input and returns `True` if the number is prime, `False` otherwise. Use this function to generate the first 10 prime numbers and store them in a list. Then, iterate through the list and execute a block of code for each prime number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True