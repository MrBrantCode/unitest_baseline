"""
QUESTION:
Create a function named `remove_duplicates` that takes an input array of strings and returns a new array containing the same strings, but with all duplicates removed, ensuring each element is unique.
"""

def remove_duplicates(arr):
    unique_arr = []
    for s in arr:
        if s not in unique_arr:
            unique_arr.append(s)
    return unique_arr