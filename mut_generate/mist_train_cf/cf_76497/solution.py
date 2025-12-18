"""
QUESTION:
Create a recursive function named `find_minimum` that takes an array of integers and returns the smallest integer in the array without using any built-in minimum functions. The array can contain any number of positive, negative integers, and zeros.
"""

def find_minimum(arr, index=0, min_num=None):
    if index == len(arr):
        return min_num
    elif min_num is None:
        min_num = arr[0]
    elif arr[index] < min_num:
        min_num = arr[index]
    return find_minimum(arr, index + 1, min_num)