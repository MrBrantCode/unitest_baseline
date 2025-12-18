"""
QUESTION:
Create a function named `search(array, string_to_locate)` that scans through the given array of strings to locate the specified string. The function should return the index of the string if found, or -1 if not found. The function should assume that the string will only appear once in the list.
"""

def search(array, string_to_locate):
    for i in range(len(array)):
        if array[i] == string_to_locate:
            return i  # Return the index where the string is found
    return -1  # Return -1 if the string is not found in the array