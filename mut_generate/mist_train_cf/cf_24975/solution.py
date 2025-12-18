"""
QUESTION:
Implement a function called `sieveOfEratosthenes(n)` that creates a data structure to store all prime numbers up to the given number `n`. The function should return a list of prime numbers. The input `n` is guaranteed to be a positive integer.
"""

import math

def sieveOfEratosthenes(n):
    prime_numbers = [True]*(n+1) 
    prime_numbers[0] = False
    prime_numbers[1] = False
      
    for i in range(2, int(math.sqrt(n)+1)): 
        if (prime_numbers[i]): 
            for j in range(i*i, n+1, i): 
                prime_numbers[j] = False
      
    return [k for k in range(n+1) if prime_numbers[k]]