"""
QUESTION:
Create a function `combine_arrays(array1, array2)` that combines two sorted arrays into a new sorted array containing only unique elements. The function should have a time complexity of O(n), where n is the total number of elements in both arrays, and a space complexity of O(n) as the output array does not count towards the space complexity.
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
        if not result or result[-1] != array1[pointer1]:  
            result.append(array1[pointer1])
        pointer1 += 1

    # Add remaining elements from Array 2
    while pointer2 < len(array2):
        if not result or result[-1] != array2[pointer2]:  
            result.append(array2[pointer2])
        pointer2 += 1

    return result