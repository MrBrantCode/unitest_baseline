"""
QUESTION:
Write a function named `find_divisors(n)` that returns a list of all positive and negative integers that are divisors of the given integer `n`, excluding zero. The function should handle both positive and negative values of `n` and return the divisors as a list, including both positive and negative divisors.
"""

def find_divisors(n):
    divisors = [] 

    for i in range(1, abs(n) + 1): 
        if n % i == 0: # If "i" divides "n"
            divisors.append(i) 
            divisors.append(-i) # Including negative divisor
            
    return divisors 