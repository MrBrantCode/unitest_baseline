"""
QUESTION:
Implement a function `max_values` that takes a two-dimensional array of integers as input and returns a one-dimensional array. The output array should contain the maximum number from each sub-array. If a sub-array is empty, the function should return -1 for that index. The function must have a time complexity of O(n), where n is the total number of elements in the input array.
"""

def max_values(arrays):
    result = []
    for array in arrays:
        if len(array) == 0:
            result.append(-1)
        else:
            result.append(max(array))
    return result