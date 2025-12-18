"""
QUESTION:
Write a function `get_lcm` that takes two integers `a` and `b` as input and returns their least common multiple (LCM). The function should also check if the inputs are prime numbers, if the LCM is a perfect square, and if the inputs are less than or equal to 10^6. If the inputs are not prime, or if they are larger than 10^6, the function should display an error message. If the LCM is a perfect square, the function should display a corresponding message.
"""

import math

def get_lcm(a, b):
    if not is_prime(a) or not is_prime(b):
        print("Both inputs should be prime numbers.")
        return
    
    if a > 10**6 or b > 10**6:
        print("Inputs should be less than or equal to 10^6.")
        return
    
    lcm = (a * b) // math.gcd(a, b)
    
    if is_perfect_square(lcm):
        print("The LCM is a perfect square.")
    else:
        print("The LCM is not a perfect square.")
    
    return lcm

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_square(n):
    root = math.isqrt(n)
    return root * root == n