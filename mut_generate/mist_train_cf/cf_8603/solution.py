"""
QUESTION:
Create a function `search_in_2d_array` that takes a two-dimensional array and an element as input, and returns a list of tuples representing the indices (row, column) where the element is found in the array. The function should return the indices in ascending order, and the rows and columns are 0-indexed.
"""

def search_in_2d_array(array, element):
    indices = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == element:
                indices.append((i, j))
    return indices