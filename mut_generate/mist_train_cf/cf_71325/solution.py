"""
QUESTION:
Create a function `is_sorted_2d(matrix)` that checks if a given two-dimensional array is sorted in ascending order, both horizontally across rows and vertically spanning columns. The function should return `True` if the array is sorted, `False` otherwise, and handle cases where the input is erroneous, such as when the input is not a list of lists of integers or when rows have different lengths. The function should be efficient and have a linear time complexity in terms of the number of elements in the 2D list.
"""

def is_sorted_2d(matrix):
    if not isinstance(matrix, list):
        return "Error: Input should be a list"
    if not all(isinstance(i, list) for i in matrix):
        return "Error: All elements of the list should also be lists"
    if not all(all(isinstance(j, int) for j in i) for i in matrix):
        return "Error: All entries should be integers"
    
    if len(matrix) == 0: 
        return True

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        return "Error: All rows should have the same length"
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            if matrix[i][j] > matrix[i][j+1]:
                return False

    for i in range(len(matrix[0])):
        for j in range(len(matrix)-1):
            if matrix[j][i] > matrix[j+1][i]:
                return False
            
    return True