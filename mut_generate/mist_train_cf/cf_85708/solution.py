"""
QUESTION:
Create a function called `merge_arrays_to_dict` that takes two arrays as input, checks if they have the same number of elements, and returns a dictionary where elements from the first array are keys and elements from the second array are values if the lengths match. If the lengths do not match, return an error message.
"""

def merge_arrays_to_dict(arr1, arr2):
    if len(arr1) != len(arr2):
        return "The arrays provided do not have an equal number of items."
    else:
        return dict(zip(arr1, arr2))