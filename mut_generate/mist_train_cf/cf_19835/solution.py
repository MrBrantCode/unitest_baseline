"""
QUESTION:
Create a function `swap_elements(array)` that takes an array of positive integers as input, swaps the elements at index 0 and index 3, and returns the modified array. The array must contain at least 5 elements. If the array is empty, or if the indices are out of range, the function should print an error message and return without modifying the array.
"""

def swap_elements(array):
    if len(array) < 5:
        print("The array must contain at least 5 elements.")
        return array
    if len(array) == 0:
        print("The array is empty.")
        return array
    array[0], array[3] = array[3], array[0]
    return array