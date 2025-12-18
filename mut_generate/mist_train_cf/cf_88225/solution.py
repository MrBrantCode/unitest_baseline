"""
QUESTION:
Write a function `merge_sorted_arrays(arr1, arr2)` that takes two sorted arrays of integers `arr1` and `arr2` and merges them into one sorted array in ascending order. The length of the input arrays can vary from 0 to 10^6. Do not use any built-in sorting functions or libraries, recursion, or divide-and-conquer algorithms. The solution should have a time complexity of O(n), where n is the total number of elements in both input arrays, and should not use any extra space except for the merged array.
"""

def merge_sorted_arrays(arr1, arr2):
    merged_arr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1

    return merged_arr