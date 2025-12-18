"""
QUESTION:
Create a function named `find_divisors(num)` that takes an integer `num` and returns a list of all its divisors in ascending order, excluding 1 and the number itself. The function should handle numbers up to 10^9 and return an empty list if the number is prime.
"""

import math

def find_divisors(num):
    divisors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            quotient = num // i
            if quotient != i:
                divisors.append(quotient)
    return sorted(divisors)