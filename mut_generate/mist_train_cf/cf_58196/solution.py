"""
QUESTION:
Create a function `array_sum` that takes two arrays of integers as input, calculates the sum of elements from both arrays manually without using any built-in or library functions, and returns the total sum. The input arrays may be of different lengths and can contain both positive and negative integers.
"""

def array_sum(array1, array2):
    total = 0
    for num in array1:
        total += num
    for num in array2:
        total += num
    return total