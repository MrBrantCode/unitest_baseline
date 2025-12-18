"""
QUESTION:
Create a function named `merge_and_sort` that takes two arrays as input and returns a new array containing all unique items from both arrays, sorted in ascending order. The input arrays can contain duplicates and be of different lengths. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the total number of elements in the input arrays.
"""

def merge_and_sort(array1, array2):
    merged_array = array1 + array2
    merged_array = list(set(merged_array))
    merged_array.sort()
    return merged_array