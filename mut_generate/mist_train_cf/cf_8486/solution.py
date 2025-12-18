"""
QUESTION:
Write a function called `concatenate_arrays` that takes two lists of integers as input, concatenates them without using any built-in array concatenation methods or functions, removes duplicate elements from the resulting list, and returns the list sorted in ascending order. The function should handle cases where the input lists contain duplicate elements.
"""

def concatenate_arrays(arr1, arr2):
    result = []
    for num in arr1 + arr2:
        if num not in result:
            result.append(num)
    result.sort()
    return result