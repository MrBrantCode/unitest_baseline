"""
QUESTION:
Create a function named `find_extreme` that takes an array of integers and an operation as parameters, where the operation is either "max" or "min". The function should return the maximum or minimum value in the array based on the operation without using any built-in standard library functions. The function should handle edge cases such as an empty array and arrays with negative numbers. The function should have a time complexity of O(n), where n is the number of elements in the array.
"""

def find_extreme(array, operation):
    if not array:
        return "Array is empty"
    extreme = array[0]
    for value in array:
        if (operation=="min" and value < extreme) or (operation=="max" and value > extreme):
            extreme = value
    return extreme