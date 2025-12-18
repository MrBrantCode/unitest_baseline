"""
QUESTION:
Create a function `is_prime` that takes a number `num` as input and returns `True` if it is prime and `False` otherwise. The function should not use any built-in functions or libraries for prime number generation or checking, and should only use basic arithmetic operations, loops, and conditional statements. The function should be optimized to minimize the number of operations required for prime number checking. Use the `is_prime` function to print all prime numbers from 1 to 100.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True