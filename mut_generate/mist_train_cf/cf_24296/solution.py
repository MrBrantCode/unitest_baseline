"""
QUESTION:
Create a function called `is_prime` that takes an integer as input and returns a boolean indicating whether the number is prime. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input number will be a positive integer.
"""

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if (num % i == 0):
                return False
    return True