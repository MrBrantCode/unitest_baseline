"""
QUESTION:
Create a function called `is_prime` that determines if a given positive integer greater than 1 is prime or composite. The function should return `True` if the number is prime and `False` if it is composite. Implement your own algorithm to check for primality without using built-in functions or libraries that directly determine if a number is prime.
"""

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True