"""
QUESTION:
Write a function named `is_prime(n)` that checks if a number `n` is prime or not. Using this function, generate and print the prime number series up to a given range limit. The function should handle numbers up to the provided limit efficiently.
"""

def is_prime(n):
    '''Check if input number is prime or not'''
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True