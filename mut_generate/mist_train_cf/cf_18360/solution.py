"""
QUESTION:
Create a function `contains_odd_prime` that determines whether an array contains an odd number of prime elements. The function should take an array of integers as input and return `True` if the array contains an odd number of prime elements, and `False` otherwise. The function should handle arrays containing both positive and negative integers, as well as edge cases such as empty arrays or arrays with only one element. The time complexity of the function should be O(n) or better.
"""

import math

def contains_odd_prime(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for num in arr:
        if num < 0:
            num = abs(num)
        if is_prime(num):
            count += 1
    return count % 2 == 1