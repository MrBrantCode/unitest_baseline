"""
QUESTION:
Create a function `is_prime(num)` to check if a given number `num` is prime. The function should return `True` if the number is prime, and `False` otherwise. The function must only use basic arithmetic operations, loops, and conditional statements, without relying on any built-in functions or libraries for prime number generation or checking. The function should also optimize the prime number checking process by minimizing the number of operations required.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True