"""
QUESTION:
Create a function `remove_duplicates(arr)` that takes an input array of strings `arr` and returns a new array with all duplicate strings removed, ensuring each element within the array is unique and not repeated.
"""

def remove_duplicates(arr):
    unique_arr = []
    for s in arr:
        if s not in unique_arr:
            unique_arr.append(s)
    return unique_arr