"""
QUESTION:
Create a function `search_element` that takes a multidimensional array and an element as input, and returns a list of tuples representing the row and column indexes of all occurrences of the element in the array. The function should use 0-based indexing for the positions.
"""

def search_element(multi_dim_array, element):
    locations = []
    for row_idx, row in enumerate(multi_dim_array):
        for col_idx, col in enumerate(row):
            if col == element:
                locations.append((row_idx, col_idx))
    return locations