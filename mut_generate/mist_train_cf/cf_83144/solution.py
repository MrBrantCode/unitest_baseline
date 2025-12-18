"""
QUESTION:
Write a function `remove_element` that takes an array of integers `arr` and an integer `elem` as input, and returns a new array containing all elements from `arr` except `elem`, in the original order. The function should not use any built-in or external library functions for array resizing or manipulation.
"""

def remove_element(arr, elem):
    i = 0  
    j = 0  

    # Traverse the array
    while j < len(arr):
        if arr[j] != elem:
            # If the current element is not the element to be removed, move it to the start of array
            arr[i] = arr[j]
            i += 1
        j += 1

    # The remaining elements of arr[:i] are the ones after removing the given element
    return arr[:i]