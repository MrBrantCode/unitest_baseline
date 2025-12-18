"""
QUESTION:
Create a function `findPrimes(array)` that takes an array of integers as input and returns a list of prime numbers greater than 10 and less than 100, sorted in descending order with no duplicates.
"""

import math

def findPrimes(array):
    primes = []
    
    for element in array:
        if 10 < element < 100:
            is_prime = True
            
            for i in range(2, int(math.sqrt(element)) + 1):
                if element % i == 0:
                    is_prime = False
                    break
            
            if is_prime and element not in primes:
                primes.append(element)
    
    return sorted(primes, reverse=True)