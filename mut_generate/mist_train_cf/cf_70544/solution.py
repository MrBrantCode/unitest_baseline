"""
QUESTION:
Construct a function named `squared_odd_primes` that generates a list of the squares of the first 'n' odd prime numbers in descending order. The function should implement an efficient algorithm to check if a number is prime, with a time complexity of O(sqrt(n)). The function should take an integer 'n' as input and return a list of squared odd prime numbers.
"""

import math

def squared_odd_primes(n):
    """
    This method generates a list of squares of first n odd prime numbers in descending order.  
    """
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num%2 == 0:
            return False
        for i in range(3, math.isqrt(num) + 1, 2): 
            if num % i == 0:
                return False
        return True

    i, count, primes = 3, 0, [] 
    while count < n:
        if is_prime(i):
            primes.append(i * i)
            count += 1
        i += 2 
    return primes[::-1] # Reverse the list for descending order