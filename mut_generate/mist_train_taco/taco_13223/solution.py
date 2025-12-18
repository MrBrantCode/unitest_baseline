"""
QUESTION:
Wilson primes satisfy the following condition.
Let ```P``` represent a prime number. 

Then ```((P-1)! + 1) / (P * P)``` should give a whole number.

Your task is to create a function that returns ```true``` if the given number is a Wilson prime.
"""

def is_wilson_prime(n):
    # List of known Wilson primes
    wilson_primes = (5, 13, 563)
    
    # Check if the given number is in the list of known Wilson primes
    return n in wilson_primes