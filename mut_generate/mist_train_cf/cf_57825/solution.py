"""
QUESTION:
Write a function called `solve` that takes a variable number of lists as input, each containing up to 20 integers between 1 and 20. The function should return a combined list with no duplicates and a boolean indicating whether all numbers in the combined list are prime numbers.
"""

def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

def solve(*args):
    combined = []
    for lst in args:
        for item in lst:
            if item not in combined:
                combined.append(item) 
    
    all_primes = all(is_prime(x) for x in combined)
    
    return combined, all_primes