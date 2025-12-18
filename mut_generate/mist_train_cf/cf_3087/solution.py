"""
QUESTION:
Create a function `is_prime_number` that takes an integer `num` as input and returns a boolean value indicating whether the number is a prime number or not. The function should return `True` if the number is prime and `False` otherwise. The implementation should not use any built-in functions or libraries to check for prime numbers and should have a time complexity of O(sqrt(n)), where n is the value of the input number `num`.
"""

def is_prime_number(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True