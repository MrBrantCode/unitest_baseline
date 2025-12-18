"""
QUESTION:
Create a function `is_prime` that takes an integer as input and returns a boolean indicating whether the number is prime or not, without using any built-in prime number checking functions or libraries. The function should handle integers less than 2 correctly and return False for these cases.
"""

def is_prime(number):
    if number < 2:  # Numbers less than 2 are not prime
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:  # If the number is divisible by any number from 2 to sqrt(number), it is not prime
            return False
    
    return True  # If the number is not divisible by any number from 2 to sqrt(number), it is prime