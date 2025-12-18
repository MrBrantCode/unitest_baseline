"""
QUESTION:
Write a function `prime_list` that takes a list of integers as input, filters out non-prime numbers, sorts the resulting list in descending order, and removes duplicates without using any built-in sorting or duplicate removal functions. The function should be able to handle large lists efficiently with a time complexity of O(n^2) or better.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_list(lst):
    result = [x for x in lst if is_prime(x)]
    result.sort(reverse=True)
    result = [result[i] for i in range(len(result)) if i == 0 or result[i] != result[i - 1]]
    return result