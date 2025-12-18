"""
QUESTION:
Implement a function called `find_common_elements(arr1, arr2)` that takes two sorted arrays as input and returns a list of common elements. The function should have a time complexity of O(n + m), where n and m are the lengths of the input arrays. The input arrays are guaranteed to be sorted in ascending order.
"""

def find_common_elements(arr1, arr2):
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result