"""
QUESTION:
Create a function called `merge_and_sort` that merges two input arrays into one and returns the resulting array sorted in ascending order. The function should take two lists of integers as input. The merged array should contain all elements from both input arrays. The resulting array should be sorted in ascending order.
"""

def merge_and_sort(array1, array2):
    # Merge the arrays
    merged_array = array1 + array2

    # Sort the merged array in ascending order
    sorted_array = sorted(merged_array)

    return sorted_array