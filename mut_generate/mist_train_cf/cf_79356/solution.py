"""
QUESTION:
Create a function `prime_operations_array` that takes no arguments and returns a three-dimensional array. The array should reflect the result of addition and multiplication operations between prime numbers within the range of 65 and 100. The first dimension of the array should represent the operation (0 for addition, 1 for multiplication), and the second and third dimensions should represent the prime numbers. The array should be populated with the results of the operations for each pair of prime numbers in the given range.
"""

import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_operations_array():
    primes = [n for n in range(65, 101) if is_prime(n)]
    array = np.empty((2, len(primes), len(primes)))
    
    for i in range(len(primes)):
        for j in range(len(primes)):
            array[0, i, j] = primes[i] + primes[j]  # addition
            array[1, i, j] = primes[i] * primes[j]  # multiplication
            
    return array