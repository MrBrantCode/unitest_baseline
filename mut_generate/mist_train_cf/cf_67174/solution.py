"""
QUESTION:
Create a function named `prime_dict` that takes a list of integers as input and returns a dictionary. The dictionary should have the integers from the input list as keys and a corresponding boolean value indicating whether the integer is prime or not. The algorithm used to check primality should have a time complexity better than O(n).
"""

import math

def is_prime(n):
    if n==1 or (n!=2 and n%2==0): 
        # 1 is not a prime number. Apart from 2, no even number is a prime number.
        return False
    for i in range(3, math.isqrt(n) + 1, 2): 
        # Only check odd numbers. Therefore, increment by 2
        if n%i==0: 
            # If divisible, then not a prime number
            return False
    return True

def prime_dict(numbers):
    return {num: is_prime(num) for num in numbers}