"""
QUESTION:
Implement a function `sort_list_descending_skip_primes(lst)` that sorts a list of integers in descending order while skipping prime numbers and removing duplicates. The function should have a time complexity of O(n log n) and a space complexity of O(1). The function should take a list of integers as input and return a new list with the composite numbers sorted in descending order.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def quick_sort_descending(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[-1]
    greater = [element for element in lst[:-1] if element > pivot and not is_prime(element)]
    lesser = [element for element in lst[:-1] if element <= pivot and not is_prime(element)]
    
    return quick_sort_descending(greater) + [pivot] + quick_sort_descending(lesser)

def sort_list_descending_skip_primes(lst):
    lst = list(set(lst)) # removing duplicates
    lst = [i for i in lst if not is_prime(i)] # skipping primes
    return sorted(lst, reverse=True) # sorting in descending order