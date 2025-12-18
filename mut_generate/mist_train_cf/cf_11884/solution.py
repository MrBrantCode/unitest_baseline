"""
QUESTION:
Write a function called "find_local_maxima" that takes a list of integers as input and returns a list of indices of all local maxima in the list. A local maximum is defined as an element greater than its immediate neighbors. The input list will have at least 3 elements and may contain duplicate elements. Return the indices of all occurrences if there are multiple occurrences of the same local maximum value.
"""

def find_local_maxima(list_vals):
    maxima_indices = []
    for i in range(1, len(list_vals) - 1):
        if list_vals[i] > list_vals[i-1] and list_vals[i] > list_vals[i+1]:
            maxima_indices.append(i)
    return maxima_indices