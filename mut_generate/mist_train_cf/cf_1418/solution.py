"""
QUESTION:
Write a function called `find_non_repeating_prime` that takes an array of integers as input and returns the first non-repeating prime number in the array. The array may contain both positive and negative integers, as well as duplicate elements. If there are no non-repeating prime numbers, the function should return `None`. The function should not use any built-in prime checking functions or libraries.
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