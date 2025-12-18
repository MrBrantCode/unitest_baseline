"""
QUESTION:
Write a function named `find_max_index` that accepts an array of positive integers as an argument. The function should return the index of the first occurrence of the item with the maximum value in the array. If there are multiple occurrences of the maximum value, return the index of the occurrence with the lowest index value. If there are no occurrences of the maximum value, return -1.
"""

def find_max_index(arr):
    max_value = max(arr)
    max_index = -1
    for i in range(len(arr)):
        if arr[i] == max_value:
            if max_index == -1 or i < max_index:
                max_index = i
    return max_index