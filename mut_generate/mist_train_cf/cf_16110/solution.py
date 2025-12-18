"""
QUESTION:
Write a function named `check_prime` that determines whether a given positive integer is prime or not. The function should return "The number is prime." if the number is prime, "The number is not prime." if the number is not prime, and "The number must be greater than 1." if the input number is less than 2. The function should only take one parameter, a positive integer named "num".
"""

import math

def check_prime(num):
    """
    This function determines whether a given positive integer is prime or not.

    Args:
        num (int): A positive integer.

    Returns:
        str: "The number is prime." if the number is prime, 
             "The number is not prime." if the number is not prime, 
             "The number must be greater than 1." if the input number is less than 2.
    """

    if num < 2:
        return "The number must be greater than 1."
    
    is_prime = True
    divisor = 2

    while divisor <= math.sqrt(num):
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        return "The number is prime."
    else:
        return "The number is not prime."