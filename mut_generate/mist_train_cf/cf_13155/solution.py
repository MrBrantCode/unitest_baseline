"""
QUESTION:
Write a function called "find_common_elements" that takes in two sorted arrays as input and returns a new array containing the common elements. The output array should also be sorted, and include all duplicate elements. Assume the input arrays will always be sorted in ascending order. Do not use any built-in functions or libraries to solve this problem.
"""

def find_common_elements(arr1, arr2):
    common_elements = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return common_elements