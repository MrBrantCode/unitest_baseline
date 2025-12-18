"""
QUESTION:
Write a function named `find_indices` that takes a list of integers as input and returns a list of indices of the maximum value in the list. If the maximum value appears multiple times, return all the corresponding indices.
"""

def find_indices(lst):
    max_val = lst[0]
    indices = []

    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            indices = []
        if lst[i] == max_val:
            indices.append(i)

    return indices