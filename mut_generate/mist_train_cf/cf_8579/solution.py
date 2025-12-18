"""
QUESTION:
Create a function named `prime_factors` that takes a positive integer `n` as input and returns a list of all prime factors of `n` excluding `n` itself, along with the count of prime factors, the sum of all prime factors, and either the product of all prime factors (if the product is greater than the sum) or the factorial of the count of prime factors (otherwise).
"""

import math

def prime_factors(n):
    factors = []
    count = 0
    total = 0
    product = 1
    
    # Check if 2 is a factor
    while n % 2 == 0:
        factors.append(2)
        count += 1
        total += 2
        product *= 2
        n = n / 2
        
    # Check for other prime factors
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            factors.append(i)
            count += 1
            total += i
            product *= i
            n = n / i
            
    # Check if the remaining number is a prime factor
    if n > 2:
        factors.append(n)
        count += 1
        total += n
        product *= n
        
    # Check if product is greater than sum
    if product > total:
        return factors, count, total, product
    else:
        return factors, count, total, math.factorial(count)