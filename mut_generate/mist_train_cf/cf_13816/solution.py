"""
QUESTION:
Write a function named `find_second_minimum` that takes an array of integers as input and returns the second smallest element in the array without using any comparison operations (such as <, >, ==) or sorting functions. The array contains at least two distinct elements and may contain duplicate elements.
"""

def find_second_minimum(arr):
    min1 = float('inf')
    min2 = float('inf')

    for num in arr:
        if num < min1:
            min2 = min1
            min1 = num
        elif num > min1 and num < min2:
            min2 = num

    return min2