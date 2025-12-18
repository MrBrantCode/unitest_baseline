"""
QUESTION:
Create a function `sumOfTwoArrays(arr1, arr2)` that takes two arrays of equal length as input and returns a new array containing the sum of corresponding elements from the two input arrays. The function should be efficient, with a time complexity of O(n), where n is the length of the input arrays.
"""

def sumOfTwoArrays(arr1, arr2):
    """Returns an array containing the sum of corresponding elements from two input arrays."""
    n = len(arr1)
    result = []
    for i in range(n):
        result.append(arr1[i] + arr2[i])
    return result