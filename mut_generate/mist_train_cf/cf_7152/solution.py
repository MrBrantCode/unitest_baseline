"""
QUESTION:
Write a function `max_positive_square` that takes an array of integers as input and returns the index and value of the maximum positive perfect square number. If no positive perfect square numbers exist, return -1 for both index and value. The function should return the index of the first occurrence of the maximum value if there are multiple positive perfect square numbers with the same maximum value. The time complexity of the function should be O(n), where n is the length of the array.
"""

import math

def max_positive_square(arr):
    max_square = -1
    max_index = -1
    
    for i, num in enumerate(arr):
        if num > 0 and math.isqrt(num) ** 2 == num:
            if num > max_square:
                max_square = num
                max_index = i
    
    return max_index, max_square