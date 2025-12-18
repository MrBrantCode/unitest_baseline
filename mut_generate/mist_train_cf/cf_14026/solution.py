"""
QUESTION:
Write a function `find_max_min(arr)` that takes an array of integers as input and returns a tuple containing the maximum and minimum values in the array. The array can have duplicate values and can be of any length between 1 and 10^6. If the array is empty, return None.
"""

def find_max_min(arr):
    if len(arr) == 0:
        return None
    
    maxValue = arr[0]
    minValue = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > maxValue:
            maxValue = arr[i]
        if arr[i] < minValue:
            minValue = arr[i]
    
    return maxValue, minValue