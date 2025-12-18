"""
QUESTION:
# Task

Given a square `matrix`, your task is to reverse the order of elements on both of its longest diagonals.

The longest diagonals of a square matrix are defined as follows:
* the first longest diagonal goes from the top left corner to the bottom right one;
* the second longest diagonal goes from the top right corner to the bottom left one.


# Example

For the matrix
```
1, 2, 3
4, 5, 6
7, 8, 9
```
the output should be:
```
9, 2, 7
4, 5, 6
3, 8, 1
```


# Input/Output


- `[input]` 2D integer array `matrix`

   Constraints: `1 ≤ matrix.length ≤ 10, matrix.length = matrix[i].length, 1 ≤ matrix[i][j] ≤ 1000`


- `[output]` 2D integer array

   Matrix with the order of elements on its longest diagonals reversed.
"""

def reverse_diagonals(matrix):
    # Create a copy of the matrix to avoid modifying the original matrix
    copy = [line[:] for line in matrix]
    
    # Get the size of the matrix (since it's a square matrix, the number of rows is equal to the number of columns)
    n = len(matrix)
    
    # Reverse the elements on the main diagonal (top-left to bottom-right)
    for i in range(n):
        copy[i][i] = matrix[n - 1 - i][n - 1 - i]
    
    # Reverse the elements on the secondary diagonal (top-right to bottom-left)
    for i in range(n):
        copy[i][n - 1 - i] = matrix[n - 1 - i][i]
    
    return copy