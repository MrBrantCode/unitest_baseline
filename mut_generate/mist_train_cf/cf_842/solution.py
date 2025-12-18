"""
QUESTION:
Implement a function merge_and_remove_duplicates(arr1, arr2) that merges two given arrays, removes duplicates, and returns the merged array in ascending order. The function should have a time complexity of O(n log n), where n is the total number of elements in the merged array, and a space complexity of O(1).
"""

def merge_and_remove_duplicates(arr1, arr2):
    merged = sorted(list(set(arr1 + arr2)))
    return merged