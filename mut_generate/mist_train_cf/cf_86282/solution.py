"""
QUESTION:
Write a function called `is_prime` that takes a positive integer `number` greater than 1 as input and returns a boolean indicating whether the number is prime and a list of its prime factors if it is not. The time complexity of the function should be less than or equal to O(sqrt(n)).
"""

import math

def is_prime(number):
    factors = []
    for divisor in range(2, int(math.sqrt(number)) + 1):
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
    
    if number > 1:
        factors.append(number)
    
    if len(factors) == 1 and factors[0] == number:
        return True, None
    else:
        return False, factors