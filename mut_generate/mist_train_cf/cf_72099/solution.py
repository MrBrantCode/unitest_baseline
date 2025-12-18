"""
QUESTION:
Write a function `prime_factors(n)` to find the prime factors of a given number `n` and their powers. The function should return a dictionary where each key-value pair represents a prime factor and the power to which it is raised in the factorization of `n`. The time complexity of the function should not exceed O(sqrt(n)).
"""

import math

def prime_factors(n):
    # Dictionary to keep track of prime number and their powers
    prime_factors = {}
  
    # Print the number of two's that divide n
    while n % 2 == 0:
        if 2 not in prime_factors:
            prime_factors[2] = 1
        else:
            prime_factors[2] += 1
        n = n / 2
        
  
    # n must be odd at this point, thus a skip of 2 can be used  
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n, print i and divide n
        while n % i== 0:
            if i not in prime_factors:
                prime_factors[i] = 1
            else:
                prime_factors[i] += 1
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        prime_factors[n] = 1
    return prime_factors