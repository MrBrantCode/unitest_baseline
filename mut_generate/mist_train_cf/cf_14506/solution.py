"""
QUESTION:
Create a function named `find_max_min` that takes an array of numbers as input and returns the minimum and maximum values. The function should have a time complexity of O(n), where n is the number of elements in the array, and should not use any built-in functions for finding the maximum and minimum values. The function should be able to handle arrays with duplicate values correctly. If the input array is empty, the function should return `None` for both the minimum and maximum values.
"""

def find_max_min(arr):
    if not arr:
        return None, None
    
    # Initialize variables to store max and min values
    max_value = arr[0]
    min_value = arr[0]
    
    # Iterate through the array
    for num in arr:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    
    return min_value, max_value