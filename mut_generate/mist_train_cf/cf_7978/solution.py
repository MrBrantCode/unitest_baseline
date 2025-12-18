"""
QUESTION:
Create a function called `is_prime` that takes an integer `number` as input and returns a boolean value indicating whether the number is prime or not. A prime number is a natural number greater than 1 that has no divisors other than 1 and itself. The function should return `True` if the number is prime and `False` otherwise. The input number can be any integer, but the function should be optimized for performance.
"""

def is_prime(number):
    '''This function should return true if the number is prime and false otherwise.'''
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True