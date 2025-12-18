"""
QUESTION:
Write a function `next_emirp(n)` that takes an integer `n` as input and returns the next emirp number greater than `n`. An emirp number is a non-palindromic prime number whose reverse is also a prime number. If no such emirp number exists, return -1. The function should be designed with maximum efficiency in mind.
"""

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_emirp(n):
    return str(n) != str(n)[::-1] and is_prime(n) and is_prime(int(str(n)[::-1]))

def next_emirp(n):
    n = n + 1
    while not is_emirp(n):
        n = n + 1
    return n