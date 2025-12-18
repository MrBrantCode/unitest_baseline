"""
QUESTION:
Write a function called `modify_array` that takes an array of integers as input, and returns the array after deleting the third element (if it exists) and shifting all the remaining elements to the left to fill the empty space. The function should not use built-in functions or methods that directly delete elements from the array. It should handle edge cases, such as an empty input array, and should have a time complexity of O(n) and space complexity of O(1), where n is the length of the input array.
"""

def modify_array(arr):
    # Check if the array has less than 3 elements
    if len(arr) < 3:
        return arr
    
    # Delete the third element by shifting all elements to the left
    for i in range(2, len(arr)):
        arr[i-1] = arr[i]
    
    # Reduce the length of the array by 1
    arr.pop()
    
    return arr