"""
QUESTION:
Combine two sorted arrays into a new array with unique elements, with a time complexity of O(n) and space complexity of O(1), where n is the total number of elements in both arrays.

The function, `combine_arrays`, should take two sorted arrays, `array1` and `array2`, as input, and return a new sorted array containing all unique elements from both arrays. The function should not use any additional data structures to store intermediate results.
"""

def combine_arrays(array1, array2):
    pointer1 = 0
    pointer2 = 0
    result = []

    while pointer1 < len(array1) and pointer2 < len(array2):
        if array1[pointer1] < array2[pointer2]:
            result.append(array1[pointer1])
            pointer1 += 1
        elif array2[pointer2] < array1[pointer1]:
            result.append(array2[pointer2])
            pointer2 += 1
        else:  # elements are equal
            result.append(array1[pointer1])
            pointer1 += 1
            pointer2 += 1

    # Add remaining elements from Array 1
    while pointer1 < len(array1):
        result.append(array1[pointer1])
        pointer1 += 1

    # Add remaining elements from Array 2
    while pointer2 < len(array2):
        result.append(array2[pointer2])
        pointer2 += 1

    return result