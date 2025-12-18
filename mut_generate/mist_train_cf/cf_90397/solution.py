"""
QUESTION:
Write a function called `modify_array` that takes an array of integers as input. If the array has less than 3 elements, the function should return the array unchanged. If the array has 3 or more elements, the function should delete the third element and shift all the remaining elements to the left to fill the empty space. The function should not use any built-in functions or methods that directly delete elements from an array, and it should handle edge cases such as an empty input array. The function should have a time complexity of O(n), where n is the length of the input array, and a space complexity of O(1), meaning it should not use additional memory proportional to the length of the input array.
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