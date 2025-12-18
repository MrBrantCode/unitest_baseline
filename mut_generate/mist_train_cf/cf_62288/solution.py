"""
QUESTION:
Implement a function named `find_distinct(matrix)` to find distinct elements in a multidimensional array. The function should take a 2D array (matrix) as input and return a dictionary where keys are distinct elements and values are their coordinates. The function should have a linear time complexity, O(n), where n is the total number of elements in the matrix.
"""

def find_distinct(matrix):
    distinct_elements = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] not in distinct_elements:
                distinct_elements[matrix[i][j]] = (i, j)
    return distinct_elements