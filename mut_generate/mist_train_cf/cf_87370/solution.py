"""
QUESTION:
Create a function `random_primes(start, end, k, n)` that takes in four integers: start, end, k, and n. The function should return a list of n random prime numbers between start and end (inclusive) that are divisible by k, along with the count of such prime numbers. If start is greater than end, return an empty list. If n is greater than the total number of prime numbers between start and end that are divisible by k, return all available prime numbers.
"""

import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def entrance(start, end, k, n):
    if start > end:
        return []
    
    primes = []
    count = 0
    for num in range(start, end + 1):
        if is_prime(num) and num % k == 0:
            primes.append(num)
            count += 1
            if count == n:
                break

    return primes[:n], count