"""
QUESTION:
Create a function `prime_factorization(num)` that takes a positive integer `num` (up to 10^9) and returns its prime factorization as a sorted list of tuples. Each tuple consists of a prime number and its corresponding exponent. The function should optimize the algorithm by only checking prime numbers up to the square root of the input number.
"""

import math

def prime_factorization(num):
    factors = []
    
    # Check for divisibility by 2
    while num % 2 == 0:
        factors.append(2)
        num = num / 2
    
    # Check for divisibility by odd numbers up to sqrt(num)
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num = num / i
    
    # If num is a prime number greater than 2
    if num > 2:
        factors.append(num)
    
    # Calculate the prime factorization as a list of tuples
    factorization = []
    for factor in set(factors):
        factorization.append((factor, factors.count(factor)))
    
    # Sort the prime factorization based on the prime numbers
    factorization.sort()
    
    return factorization