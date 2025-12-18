"""
QUESTION:
Write a function named `sum_of_sq_root` that takes an array of integers as input and returns the sum of the square roots of unique positive prime numbers in the array. The function should disregard zero, non-prime numbers, and repeated numbers. If there are no positive prime numbers in the array, the function should return 0. If the array is empty, the function should return None. The sum of square roots should be computed in the reverse order of their appearance in the array.
"""

import math
import collections

def sum_of_sq_root(arr):
    if arr is None or len(arr) == 0:
        return None

    primes_reverse_order = collections.OrderedDict()
    for num in reversed(arr):
        if num > 0 and (num == 2 or all(num % i != 0 for i in range(2, math.isqrt(num) + 1))):
            primes_reverse_order[num] = math.sqrt(num)

    return sum(primes_reverse_order.values())