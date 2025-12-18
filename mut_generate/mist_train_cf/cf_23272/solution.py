"""
QUESTION:
Write a function named `find_max_element` that takes an array of numbers as input and returns the maximum element in the array. The array is guaranteed to contain at least one element.
"""

def find_max_element(arr): 
    max_element = arr[0] 
    for index in range(1, len(arr)): 
        if arr[index] > max_element: 
            max_element = arr[index] 
    return max_element