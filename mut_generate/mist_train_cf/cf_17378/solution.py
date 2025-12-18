"""
QUESTION:
Write a function `changeCount` that takes two arrays of integers as input and returns the minimum number of changes required to transform the first array into the second array. A change is defined as modifying an element in the first array to match the corresponding element in the second array. The function should return -1 if the lengths of the two arrays are different or if more than one change is needed.
"""

def changeCount(arr1, arr2):
    if len(arr1) != len(arr2):
        return -1
    
    count = 0
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            count += 1
            if count > 1:
                return -1
    
    return count