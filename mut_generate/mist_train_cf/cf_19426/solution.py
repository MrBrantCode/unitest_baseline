"""
QUESTION:
Create a function named `custom_sort(lst)` that sorts a list of positive integers in ascending order based on the sum of their prime factors. If the sums are equal, sort them based on the number of distinct prime factors of each element. The function should be able to handle lists with up to 10^6 elements efficiently.
"""

import math

def get_prime_factors_sum(num):
    prime_factors_sum = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            prime_factors_sum += i
            num //= i
    if num > 1:
        prime_factors_sum += num
    return prime_factors_sum

def get_distinct_prime_factors(num):
    prime_factors_set = set()
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            prime_factors_set.add(i)
            num //= i
    if num > 1:
        prime_factors_set.add(num)
    return len(prime_factors_set)

def custom_sort(lst):
    return sorted(lst, key=lambda x: (get_prime_factors_sum(x), get_distinct_prime_factors(x)))