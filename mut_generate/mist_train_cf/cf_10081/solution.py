"""
QUESTION:
Create a function named `append_to_array` that takes an array `arr` and a variable number of elements to append. If the array is empty, return the message "Array is empty". Otherwise, append the elements to the end of the array and return the updated array. The function should handle any number of elements to append.
"""

def append_to_array(arr, *elements):
    if len(arr) == 0:
        return "Array is empty"
    else:
        arr.extend(elements)
        return arr