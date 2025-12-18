"""
QUESTION:
Given a NxM binary matrix consisting of 0s and 1s. Find if there exists a rectangle/ square within the matrix whose all four corners are 1. 
Example 1:
Input:
N = 4, M = 5
matrix[][] = 
{
{1 0 0 1 0},
{0 0 1 0 1},
{0 0 0 1 0}, 
{1 0 1 0 1}
} 
Output: Yes
Explanation:
Valid corners are at index (1,2), (1,4), (3,2), (3,4) 
Example 2:
Input:
N = 3, M = 3
matrix[][] = 
{{0 0 0},
{0 0 0},
{0 0 0}}
Output: No
Your Task:
You don't need to take input or print anything. Complete the function ValidCorners() that takes the given matrix as input parameter and returns a boolean value.
Constraints:
1 <= R, C <= 200
0 <= A[i] <= 1
"""

def has_rectangle_with_corners(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                for k in range(i + 1, n):
                    if matrix[k][j] == 1:
                        for l in range(j + 1, m):
                            if matrix[i][l] == 1 and matrix[k][l] == 1:
                                return True
    return False