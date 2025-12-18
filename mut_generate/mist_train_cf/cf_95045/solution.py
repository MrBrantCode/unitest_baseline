"""
QUESTION:
Create a function called `find_minimum` that takes an array of positive integers as input and returns the minimum element within the array. You cannot use built-in functions or methods that directly provide the minimum element of an array. The function must have a time complexity of O(n) and handle arrays containing at least one element and no more than 10^6 elements.
"""

def find_minimum(arr):
    minimum = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    
    return minimum