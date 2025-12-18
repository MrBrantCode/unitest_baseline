"""
QUESTION:
Implement a function named `find_evens` that takes a multi-dimensional list of integers as input and returns a list of tuples, where each tuple contains an even number from the input list and its corresponding index. The index is represented as a tuple, where the size of the tuple corresponds to the level of nesting in the original array. The function should be able to handle arrays of varying dimensions and should return the even numbers along with their indices in the original multi-dimensional array.
"""

def find_evens(arr, index=()):
    result = []  
    # iterate over the array and its indices
    for i, x in enumerate(arr):
        # if an element is a list, recur, updating the index
        if isinstance(x, list):
            result.extend(find_evens(x, index + (i,)))
        # if an element is an even number, append it and its index
        elif x % 2 == 0:
            result.append((x, index + (i,)))
    return result