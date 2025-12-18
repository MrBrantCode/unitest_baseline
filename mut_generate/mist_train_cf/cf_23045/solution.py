"""
QUESTION:
Implement a function `rotate_2d_array(matrix)` that rotates a given 2D array 90 degrees clockwise using only basic Python operations and data structures. The function should work recursively and handle arrays with any number of rows and columns, including those with duplicate values.
"""

def rotate_2d_array(matrix):
    if not matrix:
        return matrix
    
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new rotated matrix
    rotated_matrix = [[0] * rows for _ in range(cols)]
    
    # Recursive helper function to rotate each element
    def rotate_element(i, j):
        if j >= cols:
            return
        
        rotated_matrix[j][rows - 1 - i] = matrix[i][j]
        
        if i + 1 < rows:
            rotate_element(i + 1, j)
        elif j + 1 < cols:
            rotate_element(0, j + 1)
    
    # Start rotation from the top-left element
    rotate_element(0, 0)
    
    return rotated_matrix