"""
QUESTION:
Write a function `find_smallest_primes_with_sum(array, value)` that takes an array of positive integers and a target value as input, and returns the two smallest prime numbers in the array that sum up to the given value. If no such pair is found, return "No pair found."
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_smallest_primes_with_sum(array, value):
    primes = [num for num in array if is_prime(num)]
    primes.sort()
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i] + primes[j] == value:
                return [primes[i], primes[j]]
    return "No pair found."