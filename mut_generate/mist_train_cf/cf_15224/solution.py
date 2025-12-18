"""
QUESTION:
Write a function called `find_intersect(arr1, arr2)` that returns all intersecting elements between two arrays `arr1` and `arr2`. The function should have a time complexity of O(n), where n is the length of the arrays, and should not use any built-in intersection functions or data structures. The function should use only constant extra space, without modifying the input arrays.
"""

def find_intersect(arr1, arr2):
    intersect = []
    arr1_set = set(arr1)
    for num in arr2:
        if num in arr1_set:
            intersect.append(num)
    return intersect