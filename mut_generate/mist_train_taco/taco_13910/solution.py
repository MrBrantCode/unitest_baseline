"""
QUESTION:
Given a binary matrix of dimensions  with R rows and C columns. Start from cell(0, 0), moving in the right direction. Perform the following operations: 
	If the value of matrix[i][j] is 0, then traverse in the same direction and check the next value.
	If the value of matrix[i][j] is 1, then update matrix[i][j] to 0 and change the current direction clockwise. ie - up, right, down, or left directions change to right, down, left, and up respectively.
Find the index of the cell where you will be forced to exit the matrix while performing the given traversal. 
Example 1:
Input:
matrix[][] = {{0,1},
              {1,0}}
R=2
C=2
Output: (1,1)
Explanation:
Example 2:
Input: 
matrix[][] = {{0, 1, 1, 1, 0},
                   {1, 0, 1, 0, 1},
              {1, 1, 1, 0, 0}}
R=3
C=5
Output: (2,0)
Explanation: We will leave the grid after visiting the index (2,0).
 
Your Task:
You don't need to read input or print anything. Complete the function endPoints() which take a 2D matrix[][] , an integer R and an integer C as input parameters and returns the index of the last cell before exiting the matrix. 
Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
Constraints:
1<= R,C<=1000
0<= matrix[i][j] <=1
"""

def find_exit_point(matrix, R, C):
    # Starting position and initial direction
    y, x, m = 0, 0, 0
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while True:
        # Traverse in the current direction until a boundary or a 1 is encountered
        while 0 <= y < R and 0 <= x < C and matrix[y][x] == 0:
            y += move[m][0]
            x += move[m][1]
        
        # Check if we have exited the matrix
        if y < 0 or y == R or x < 0 or x == C:
            return (y - move[m][0], x - move[m][1])
        else:
            # Update the cell to 0 and change direction
            matrix[y][x] = 0
            m = (m + 1) % 4