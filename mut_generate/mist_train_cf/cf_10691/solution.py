"""
QUESTION:
Create a function `get_prime_divisors(num)` that takes an integer `num` as input and returns a set of its prime divisors. The function should only consider divisors up to the square root of `num` and check for primality by testing divisibility up to the square root of the potential divisor.
"""

import math

def get_prime_divisors(num):
    prime_divisors = set()
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_divisors.add(i)
            # Add the other divisor if it is prime
            other_divisor = num // i
            is_prime = True
            for j in range(2, int(math.sqrt(other_divisor)) + 1):
                if other_divisor % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_divisors.add(other_divisor)
    
    return prime_divisors