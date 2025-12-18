"""
QUESTION:
Write a function `check_product_coprime` that takes a list of positive integers as input and returns `True` if the product of all numbers in the list is a prime number (only divisible by 1 and itself, and greater than 1) and `False` otherwise. The solution should have optimal time complexity.
"""

import math

def is_prime(n):
    # Returns True if n is a prime number. A prime number is only divisible by 1 and itself
    if n<=1:
        return False
    elif n <= 3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i = 5
    while(i**2 <= n):
        if(n%i==0 or n%(i+2)==0):
            return False
        i += 6
    return True

def check_product_coprime(list):
    # product of all elements in the list
    product = math.prod(list)
    # Check whether the product is prime
    return is_prime(product)