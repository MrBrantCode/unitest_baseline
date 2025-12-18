"""
QUESTION:
Create a function `merge_sort_count` that takes two sorted arrays `arr1` and `arr2` as input and returns a tuple containing the merged sorted array and the total number of inversions. An inversion occurs when a value from `arr2` is inserted before a value from `arr1`. The function should have a time complexity of O(n), where n is the total number of elements in both arrays.
"""

def merge_sort_count(arr1, arr2):
    i = j = inv_count = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else: 
            result.append(arr2[j])
            inv_count += len(arr1) - i
            j += 1
    result += arr1[i:]
    result += arr2[j:]
    return result, inv_count