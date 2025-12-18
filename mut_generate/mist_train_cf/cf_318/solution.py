"""
QUESTION:
Implement a function named `reverse` that takes an array of integers as input and returns the array with its elements in reverse order. The input array will contain at least 10 elements and at most 1000 elements. The array elements will be integers between -100 and 100. The function should reverse the order of duplicate elements while maintaining the overall order of the other elements. The function should not use any built-in array reverse functions.
"""

def reverse(arr):
    # Create an empty result array
    result = []
    
    # Iterate through the input array in reverse order
    for i in range(len(arr)-1, -1, -1):
        # If the current element is not already in the result array, add it
        if arr[i] not in result:
            result.append(arr[i])
    
    return result