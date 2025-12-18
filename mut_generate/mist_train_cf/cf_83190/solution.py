"""
QUESTION:
Write a Python function named `prime_multiply` that takes an integer `a` (less than 10,000) and returns a dictionary containing a list of distinct prime factors and their sum if `a` is a product of exactly three distinct prime numbers. Otherwise, return a dictionary with an empty list of factors and a sum of `None`.
"""

def prime_multiply(a):
    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97
    ]

    factors = []
    temp = a

    for prime in primes:
        if temp % prime == 0:
            while temp % prime == 0:
                if prime not in factors:
                    factors.append(prime)
                temp = temp // prime

    if len(factors) == 3 and temp == 1:
        return {"factors": factors, "sum": sum(factors)}
    else:
        return {"factors": [], "sum": None}