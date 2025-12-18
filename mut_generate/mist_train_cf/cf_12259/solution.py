"""
QUESTION:
Create a function `remove_duplicates` that takes an array as input and returns a new array containing only unique elements from the input array. The function must not use any built-in methods or data structures (such as sets or dictionaries) to store unique values. The original order of elements in the input array should be preserved in the output array.
"""

def remove_duplicates(arr):
    unique_arr = []
    for element in arr:
        if element not in unique_arr:
            unique_arr.append(element)
    return unique_arr