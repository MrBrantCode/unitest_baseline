"""
QUESTION:
Write a function named `primeFactors` that calculates the prime factors of a given number `n`, optimized to handle large numbers efficiently. The function should return the prime factorization as a string in ascending order, including the power of each factor if applicable (e.g., "2^3, 3"). The function should have a time complexity of O(sqrt(n)) or better, and it is not required to use memoization due to the efficiency of the algorithm.
"""

from collections import defaultdict
import math

def primeFactors(n): 
    factors = defaultdict(int)
    
    # Print the number of two's that divide n
    while n % 2 == 0: 
        factors[2] += 1
        n = n / 2
          
    # n must be odd at this point, thus skip the even numbers and iterate only for odd
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n, print i and divide n
        while n % i== 0: 
            factors[i] += 1
            n = n / i 
              
    # Condition if n is a prime number greater than 2
    if n > 2: 
        factors[n] += 1
    
    # Building factorization string representation
    res = []
    for k, v in sorted(factors.items()):
        if v == 1:
            res.append(f"{int(k)}")
        else:
            res.append(f"{int(k)}^{v}")
    return ", ".join(res)