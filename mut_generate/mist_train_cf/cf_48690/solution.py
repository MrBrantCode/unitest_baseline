"""
QUESTION:
Write a function called `last_elements` that takes a 2D array as input and returns a list of the last elements of each sub-array in the original order. If a sub-array is empty, return 'Empty Sub-array' instead.
"""

def last_elements(mylist):
    result = []
    for subarray in mylist:
        if subarray:
            result.append(subarray[-1])
        else:
            result.append('Empty Sub-array')
    return result