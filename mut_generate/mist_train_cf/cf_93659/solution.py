"""
QUESTION:
Create a function `is_prime_with_three_distinct_factors` that takes an integer `number` as input and returns `True` if the number is prime and has exactly three distinct prime factors, and `False` otherwise. The function should be efficient and handle large inputs.
"""

import math

def is_prime_with_three_distinct_factors(number):
    # Check if the number is prime
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    # Check if the number has exactly three distinct prime factors
    distinct_factors = set()
    prime_factors = []
    factor = 2
    while factor <= math.sqrt(number):
        if number % factor == 0:
            if factor not in distinct_factors:
                distinct_factors.add(factor)
                prime_factors.append(factor)
            number = number / factor
        else:
            factor += 1
    if number > 1 and number not in distinct_factors:
        prime_factors.append(int(number))
    
    return len(distinct_factors) == 3 and len(prime_factors) == 3