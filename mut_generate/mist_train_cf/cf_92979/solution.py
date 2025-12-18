"""
QUESTION:
Write a function called merge_and_sort that takes two arrays of integers as input. The function should return a new array containing all unique integers from both input arrays in ascending order. The function should have a time complexity of O(n log n) and space complexity of O(n), where n is the total number of elements in the input arrays.
"""

def merge_and_sort(array1, array2):
    merged_array = list(set(array1 + array2))
    merged_array.sort()
    return merged_array