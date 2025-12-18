"""
QUESTION:
Write a function `sum_of_primes` that takes three parameters `n`, `m`, and `x`, and returns the sum of the first `n` prime numbers starting with `m`, where each prime number must be greater than `x`. The function should return an integer value representing the sum of the first `n` prime numbers meeting the given conditions.
"""

def sum_of_primes(n, m, x):
    primes = []  
    num = m  
    
    while len(primes) < n:
        is_prime = True
        
        # Check if num is a prime number
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        # If num is prime and greater than x, add it to the list of primes
        if is_prime and num > x:
            primes.append(num)
        
        num += 1  
    
    return sum(primes)  