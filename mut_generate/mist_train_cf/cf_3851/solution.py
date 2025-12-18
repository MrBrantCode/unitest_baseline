"""
QUESTION:
Create a function called `combine_arrays` that combines two input arrays `arr1` and `arr2` into a single array. The resulting array must contain unique elements, be sorted in ascending order, and have a time complexity of O(n), where n is the total number of elements in both input arrays. The solution should not use any additional data structures to store intermediate results.
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