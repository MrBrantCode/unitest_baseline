"""
QUESTION:
Create a function `is_prime(num)` that takes an integer `num` as input and returns a boolean indicating whether the number is prime or not. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input number can be any integer.
"""

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return num > 1