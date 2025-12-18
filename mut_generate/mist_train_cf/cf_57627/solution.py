"""
QUESTION:
Construct a function `arrange_array(array)` that takes an array of integers as input and returns a sequence of these integers such that the sum of any two adjacent elements is a prime number. The input array may contain positive and negative integers, as well as zeros. If such a sequence cannot be formed, return an error message.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

from itertools import permutations

def arrange_array(array):
    perms = permutations(array)
    for perm in perms:
        for i in range(len(perm) - 1):
            if not is_prime(perm[i] + perm[i+1]):
                break
        else:
            return list(perm)
    return "No valid sequence found"