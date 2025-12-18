"""
QUESTION:
Write a function `countDistinctPrimes` that takes a list of integers as input and returns the count of distinct prime numbers in the list. The list is considered valid if it is sorted in descending order and contains only prime numbers (including duplicates). The function should return the count of distinct prime numbers present in the list.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def countDistinctPrimes(nums):
    distinctPrimes = 0
    prevPrime = 0
    for num in nums:
        if is_prime(num) and num > prevPrime:
            distinctPrimes += 1
            prevPrime = num
    return distinctPrimes