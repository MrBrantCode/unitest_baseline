"""
QUESTION:
Write a function `find_first_max_index` that accepts an array of positive integers as an argument. The function should return the index of the first occurrence of the item with the maximum value. If there are multiple occurrences of the maximum value, return the index of the occurrence with the lowest index value. If the input array is empty, return -1. Implement the solution using a single loop and without using built-in functions such as max().
"""

def find_first_max_index(arr):
    if len(arr) == 0:
        return -1
    max_val = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
        elif arr[i] == max_val:
            if i < max_index:
                max_index = i
    return max_index