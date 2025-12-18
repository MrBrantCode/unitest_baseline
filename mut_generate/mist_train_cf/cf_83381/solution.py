"""
QUESTION:
Write a Python function named `sort_3D_list` that sorts a given 3D list in ascending order based on the ordinal value of the third character in each secondary-level array. If the secondary array has fewer than 3 elements, use 0 as the sorting key.
"""

def sort_3D_list(arr):
    arr.sort(key=lambda x: ord(x[1][2]) if len(x[1]) > 2 else 0)
    return arr