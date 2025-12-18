"""
QUESTION:
Create a function `contains_odd_prime` that takes an array of integers as input and returns `True` if the array contains an odd number of prime elements, and `False` otherwise. The function should handle arrays containing both positive and negative integers, as well as edge cases such as an empty array or an array with only one element, and should have a time complexity of O(n) or better.
"""

import math

def contains_odd_prime(arr):
    count = 0
    for num in arr:
        if num < 0:
            num = abs(num)
        if num < 2:
            continue
        if num == 2:
            count += 1
            continue
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            count += 1
    return count % 2 == 1