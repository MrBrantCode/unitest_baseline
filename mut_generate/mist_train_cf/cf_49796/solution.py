"""
QUESTION:
Write a function `maxPrimeProduct` that takes an array of integers as input and returns the maximum product of three integers in the array that is a prime number. If no such product exists, return -1.
"""

def maxPrimeProduct(arr):
    # Find all unique elements and save them with their counts in a dictionary
    count = {}
    for el in arr:
        if el not in count:
            count[el] = 1
        else:
            count[el] += 1
    
    # List of prime numbers less than 10
    primes = [2, 3, 5, 7]

    # If '1' is in list and there exists another same prime number
    # twice or more in list, then product exists
    if 1 in count:
        for prime in primes:
            if prime in count and count[prime] >= 2:
                return prime*prime
            elif -prime in count and count[-prime] >= 2:
                return -prime*-prime

    # If no such case exists, return -1
    return -1