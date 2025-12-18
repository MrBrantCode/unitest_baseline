"""
QUESTION:
Create a function called `contains_in_order` that takes two arrays of integers as input and returns a boolean value. The function should return True if the first array contains all the elements in the second array in the same order, without any other elements in between, and False otherwise. The function should not use any built-in functions or methods that directly solve this problem.
"""

def contains_in_order(arr1, arr2):
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            j += 1
        i += 1
    return j == len(arr2)