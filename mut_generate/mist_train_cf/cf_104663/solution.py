"""
QUESTION:
Create a function `is_prime(num)` that takes an integer as input and returns a boolean indicating whether the number is prime or composite. The number to be checked will be a random integer between 1 and 1000. The function should be able to handle numbers up to 1000.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True