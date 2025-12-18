"""
QUESTION:
Write a function `find_max(array)` that finds the maximum number in an array without using the built-in `max()` function. The function should have a time complexity of O(n), where n is the number of elements in the array. The input array contains at least one element.
"""

def entrance(array):
    # Initialize the maximum number as the first element in the array
    max_number = array[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(array)):
        # If the current element is greater than the current maximum number, update the maximum number
        if array[i] > max_number:
            max_number = array[i]
    
    return max_number