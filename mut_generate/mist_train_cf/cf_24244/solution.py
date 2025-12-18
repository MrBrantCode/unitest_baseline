"""
QUESTION:
Write a function named `common_elements` that takes two arrays of integers, `arr1` and `arr2`, as input and returns a list of their common elements. The function should not include duplicate values in the output list, and the order of elements does not matter.
"""

def common_elements(arr1, arr2):
    result = []
    for numbers in arr1:
        if numbers in arr2 and numbers not in result:
            result.append(numbers)
    return result