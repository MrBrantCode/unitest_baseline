"""
QUESTION:
Write a function named `find_string_depth` that takes a multi-dimensional array and a target string as input. The function should return the depth level at which the target string is found, or -1 if the string is not found in the array. The function should be able to handle arrays of varying depths.
"""

def find_string_depth(arr, target):
    for element in arr:
        if element == target:
            return 0
        elif isinstance(element, list):
            depth = find_string_depth(element, target)
            if depth != -1:
                return 1 + depth
    return -1