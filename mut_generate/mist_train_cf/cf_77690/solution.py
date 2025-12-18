"""
QUESTION:
Write a function `find_unique(matrix)` that identifies and locates multiple unique entities in a given multidimensional array `matrix`. The function should return the unique entities and their locations. The time complexity should be as efficient as possible, ideally O(n) where n is the total number of elements in the 2D array.
"""

def find_unique(matrix):
    """
    Function to find and locate multiple unique entities in a multidimensional array
    """
    unique_elements = set()
    locations = dict()

    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem not in unique_elements:
                unique_elements.add(elem)
                locations[elem] = [(i, j)]
            else:
                locations[elem].append((i, j))
    return {key: value for key, value in locations.items() if len(value) == 1}