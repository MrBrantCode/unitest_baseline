"""
QUESTION:
Write a function named `find_min` that takes an array of at least one positive integer as input and returns the minimum element in the array. The solution must have a time complexity of O(n) and cannot use any built-in functions or methods to find the minimum element, nor any additional data structures or variables apart from the input array and loop variables.
"""

def find_min(arr):
    min_val = arr[0]  
    for i in range(1, len(arr)):  
        if arr[i] < min_val:  
            min_val = arr[i]
    return min_val