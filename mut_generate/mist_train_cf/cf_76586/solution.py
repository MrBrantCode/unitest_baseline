"""
QUESTION:
Write a function named `find_min_disparity` that takes an array of elements as input, identifies the pair of elements with the smallest absolute difference, and returns the difference along with the pair. The function should handle arrays containing a mix of integers and floating point numbers, ignore non-numeric elements, and return a suitable message for edge cases where the array is empty or contains only one element.
"""

def find_min_disparity(arr):
    # Filter out non-numeric elements
    arr = [x for x in arr if isinstance(x, (int, float))]
    
    # Handle edge cases
    if len(arr) == 0:
        return "Array is empty"
    elif len(arr) == 1:
        return "Array contains only one element"
    
    # Sort the array
    arr.sort()
    
    # Initialize variables
    min_disparity = float('inf')
    pair = (None, None)
    
    # Find the pair of elements with minimum disparity
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < min_disparity:
            min_disparity = arr[i+1] - arr[i]
            pair = (arr[i], arr[i+1])
    
    return min_disparity, pair