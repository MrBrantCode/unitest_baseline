"""
QUESTION:
Create a Python function called `find_duplicates` that takes a two-dimensional matrix as input, where the matrix contains tuples of varying lengths with both numeric and non-numeric elements. The function should return a list of duplicates, where each duplicate is represented as a tuple containing the row index, column index, and the duplicated tuple itself. The function should treat tuples with identical elements in different orders as non-duplicates.
"""

def find_duplicates(matrix):
    # Create a set to store tuple elements
    elements_set = set()

    # Create a list to store duplicates
    duplicates = []

    # iterate over the matrix
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            # Check if tuple is in set of elements
            if element in elements_set:
                # If element is in set, add it to the list of duplicates
                duplicates.append((i, j, element))
            else:
                # If not, add element to set of seen elements
                elements_set.add(element)

    # return list of duplicates
    return duplicates