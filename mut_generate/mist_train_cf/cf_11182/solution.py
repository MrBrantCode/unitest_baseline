"""
QUESTION:
Create a function `find_minimum` that takes an array as input and returns the minimum element within the array without using any built-in functions or methods that directly provide the minimum element of an array. The input array is guaranteed to contain at least one element.
"""

def find_minimum(arr):
    min_element = arr[0]  # Assume the first element is the minimum
    
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
    
    return min_element