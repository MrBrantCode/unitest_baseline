"""
QUESTION:
Create a function `HasCloseElements` that takes two parameters: an array of floating-point numbers and a threshold number. The function should return `True` if any two numbers in the array are closer to each other than the specified threshold, and `False` otherwise.
"""

import math

def HasCloseElements(nums, threshold):
    length = len(nums)
    for i in range(length - 1):
        for j in range(i+1, length):
            if abs(nums[i] - nums[j]) < threshold:
                return True
    return False