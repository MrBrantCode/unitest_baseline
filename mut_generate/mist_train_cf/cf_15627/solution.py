"""
QUESTION:
Create a function named `merge_and_sort` that takes two arrays `arr1` and `arr2` as input, merges them into a new array, removes any duplicate elements, and returns the new array sorted in ascending order. The function should handle cases where the input arrays contain duplicate elements or are empty.
"""

def merge_and_sort(arr1, arr2):
    merged = arr1 + arr2  # concatenate the two arrays
    merged = list(set(merged))  # remove duplicates by converting to set and then back to list
    merged.sort()  # sort the array in ascending order
    return merged