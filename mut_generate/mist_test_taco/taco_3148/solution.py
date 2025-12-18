"""
QUESTION:
Given a boolean matrix of size RxC where each cell contains either 0 or 1, find the row numbers of row (0-based) which already exists or are repeated.
Example 1:
Input:
R = 2, C = 2
matrix[][] = {{1, 0},
              {1, 0}}
Output: 
1
Explanation:
Row 1 is duplicate of Row 0.
Example 2:
Input:
R = 4, C = 3
matrix[][] = {{ 1, 0, 0},
              { 1, 0, 0},
              { 1, 0, 0},
              { 0, 0, 0}}
Output: 
1 2 
Explanation:
Row 1 and Row 2 are duplicates of Row 0. 
Your Task:
You dont need to read input or print anything. Complete the function repeatedRows() that takes the matrix as input parameter and returns a list of row numbers which are duplicate rows.
 
Expected Time Complexity: O(R * C)
Expected Auxiliary Space: O(R*C) 
 
Constraints:
1 ≤ R ≤ 1000
1 ≤ C ≤ 20
0 ≤ matrix[i][j] ≤ 1
"""

def find_duplicate_rows(matrix, R, C):
    row_count = {}
    duplicate_rows = []
    
    for i in range(R):
        row_tuple = tuple(matrix[i])
        if row_tuple in row_count:
            row_count[row_tuple] += 1
            if row_count[row_tuple] == 2:
                duplicate_rows.append(i)
        else:
            row_count[row_tuple] = 1
    
    return duplicate_rows