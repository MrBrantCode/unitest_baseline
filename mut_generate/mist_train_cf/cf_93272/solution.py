"""
QUESTION:
Create a function `find_max_min` that takes a list of numbers as input and returns the minimum and maximum values in the list. The function should not use built-in functions for finding the maximum and minimum values and should have a time complexity of O(n), where n is the number of elements in the list. If the input list is empty, the function should return `None, None`.
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