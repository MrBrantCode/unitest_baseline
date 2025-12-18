"""
QUESTION:
Write a function `findMax` that takes an array `arr` as input and returns the maximum element in the array. The function should have a time complexity of O(n), where n is the number of elements in the input array, and should not use any built-in functions, methods, or additional data structures. The function should handle edge cases such as an empty input array, an array with all elements being the same, and an array with all elements being negative or positive. If there are multiple occurrences of the maximum element, the function should return the first occurrence.
"""

def findMax(arr):
    # Check for empty input array
    if len(arr) == 0:
        return None
    
    # Initialize maxElement as the first element of the array
    maxElement = arr[0]
    
    # Iterate over each element in the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is greater than maxElement
        if arr[i] > maxElement:
            # Update maxElement
            maxElement = arr[i]
    
    # Return the maximum element
    return maxElement