"""
QUESTION:
Create a function called `is_2d_array_ordered(matrix)` that takes a 2D array (list of lists) as input and returns a boolean value indicating whether the array is ordered. The array is considered ordered if every element is less than or equal to the elements to its right and below it, i.e., the array is in ascending order both row-wise and column-wise. The function should assume that the input 2D array is a list of lists where each inner list (i.e., row) has the same length.
"""

def is_2d_array_ordered(matrix):
    # get the number of rows and columns
    rows, cols = len(matrix), len(matrix[0])
    
    # check each element
    for i in range(rows):
        for j in range(cols):
            # check right neighbor if exists
            if j < cols - 1 and matrix[i][j] > matrix[i][j+1]:
                return False
            
            # check below neighbor if exists
            if i < rows - 1 and matrix[i][j] > matrix[i+1][j]:
                return False
                
    # if no out-of-order elements found, return True
    return True