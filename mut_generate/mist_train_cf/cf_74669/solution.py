"""
QUESTION:
Write a function `isolate_primes` that takes a list of integers as input and returns a new list containing only the prime numbers from the input list, in descending order. The function should not use any pre-existing library functions to check for primality.
"""

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def isolate_primes(lst):
    primes = [num for num in lst if is_prime(num)]
    primes.sort(reverse=True)
    return primes