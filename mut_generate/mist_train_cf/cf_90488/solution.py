"""
QUESTION:
Create a function `search_in_2d_array` that takes a two-dimensional array and an element as input and returns a list of tuples, where each tuple represents the indices (row, column) of the element in the array. The function should return all occurrences of the element, and the indices should be in ascending order. The rows and columns are 0-indexed.
"""

def search_in_2d_array(array, element):
    indices = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == element:
                indices.append((i, j))
    return indices