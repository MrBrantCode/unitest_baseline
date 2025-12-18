"""
QUESTION:
Combine two sorted arrays into a new sorted array containing unique elements. Implement a function `combine_arrays(arr1, arr2)` that takes two sorted arrays `arr1` and `arr2` as input and returns a new sorted array containing unique elements from both arrays. The function should not use any additional data structures to store intermediate results and should achieve an overall time complexity of O(n), where n is the total number of elements in both arrays.
"""

def combine_arrays(arr1, arr2):
    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements from arr1, if any
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Add remaining elements from arr2, if any
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result