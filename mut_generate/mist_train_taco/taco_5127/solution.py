"""
QUESTION:
Given a boolean matrix of size RxC where each cell contains either 0 or 1, modify it such that if a matrix cell matrix[i][j] is 1 then all the cells in its i^{th} row and j^{th} column will become 1.
Example 1:
Input:
R = 2, C = 2
matrix[][] = {{1, 0},
              {0, 0}}
Output: 
1 1
1 0 
Explanation:
Only cell that has 1 is at (0,0) so all 
cells in row 0 are modified to 1 and all 
cells in column 0 are modified to 1.
Example 2:
Input:
R = 4, C = 3
matrix[][] = {{ 1, 0, 0},
              { 1, 0, 0},
              { 1, 0, 0},
              { 0, 0, 0}}
Output: 
1 1 1
1 1 1
1 1 1
1 0 0 
Explanation:
The position of cells that have 1 in
the original matrix are (0,0), (1,0)
and (2,0). Therefore, all cells in row
0,1,2 are and column 0 are modified to 1. 
Your Task:
You dont need to read input or print anything. Complete the function booleanMatrix() that takes the matrix as input parameter and modifies it in-place.
 
Expected Time Complexity: O(R * C)
Expected Auxiliary Space: O(R + C) 
 
Constraints:
1 ≤ R, C ≤ 1000
0 ≤ matrix[i][j] ≤ 1
"""

def update_boolean_matrix(matrix):
    if not matrix or not matrix[0]:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Flags to track if the first row and first column need to be updated
    first_row_has_one = any(matrix[0][c] == 1 for c in range(cols))
    first_col_has_one = any(matrix[r][0] == 1 for r in range(rows))
    
    # Mark the first row and first column based on the rest of the matrix
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 1:
                matrix[r][0] = 1
                matrix[0][c] = 1
    
    # Update the matrix based on the marked first row and first column
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 1 or matrix[0][c] == 1:
                matrix[r][c] = 1
    
    # Update the first row if needed
    if first_row_has_one:
        for c in range(cols):
            matrix[0][c] = 1
    
    # Update the first column if needed
    if first_col_has_one:
        for r in range(rows):
            matrix[r][0] = 1