"""
QUESTION:
Write a function `findCommonElements` that takes two arrays of integers as input and returns an array containing the common elements found in both input arrays. The function should return an empty array if there are no common elements. The solution must have a time complexity of O(n), where n is the total number of elements in both input arrays.
"""

def findCommonElements(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    return [num for num in set1 if num in set2]