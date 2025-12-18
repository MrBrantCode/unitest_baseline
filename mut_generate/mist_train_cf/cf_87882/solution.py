"""
QUESTION:
Write a function `find_min(arr)` that takes an array of at least one positive integer and computes the minimum element within the array. The solution must have a time complexity of O(n), cannot use any built-in functions or methods that directly provide the minimum element of an array, and cannot use any additional data structures or variables apart from the input array and the loop variables.
"""

def find_min(arr):
    min_val = arr[0]  
    for i in range(1, len(arr)):  
        if arr[i] < min_val:  
            min_val = arr[i]
    return min_val