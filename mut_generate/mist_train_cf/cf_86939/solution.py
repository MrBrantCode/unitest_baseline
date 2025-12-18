"""
QUESTION:
Write a function `find_non_repeating_prime(arr)` that finds the first non-repeating prime number in a given array. The array can contain both positive and negative integers and may have duplicate elements. If there are no non-repeating prime numbers, return None. The algorithm should not use any built-in prime checking functions or libraries. The time complexity should be O(n^2).
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_non_repeating_prime(arr):
    count = {}
    for num in arr:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    
    for num in arr:
        if count[num] == 1 and is_prime(num):
            return num
    
    return None