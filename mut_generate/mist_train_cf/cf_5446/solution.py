"""
QUESTION:
Write a function `find_maximum` that returns the maximum number from a given array of integers, considering absolute values, without using built-in max functions, sorting, or additional data structures, and with a time complexity of O(n). The function should return the maximum value that occurs first in the array if there are multiple maximum values with the same absolute value. The array may contain negative integers.
"""

def find_maximum(arr):
    maximum = None
    
    for num in arr:
        if maximum is None or abs(num) > abs(maximum):
            maximum = num
    
    return maximum