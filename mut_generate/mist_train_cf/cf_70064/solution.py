"""
QUESTION:
Given a set of unique prime numbers, write a function `check_primes` that checks if the sum of any two primes in the set results in a composite number.
"""

def check_primes(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_prime(lst[i] + lst[j]):
                return True
    return False

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True