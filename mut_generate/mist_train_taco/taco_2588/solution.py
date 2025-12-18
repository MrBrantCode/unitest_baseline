"""
QUESTION:
Given a square matrix of size N x N. The task is to find the determinant of this matrix.
Example 1:
Input:
N = 4
matrix[][] = {{1, 0, 2, -1},
              {3, 0, 0, 5},
              {2, 1, 4, -3},
              {1, 0, 5, 0}}
Output: 30
Explanation:
Determinant of the given matrix is 30.
Example 2:
Input:
N = 3
matrix[][] = {{1, 2, 3},
              {4, 5, 6},
              {7, 10, 9}}
Output: 12
Explanation:
Determinant of the given matrix is 12.
Your Task:
You don't need to read input or print anything. Complete the function determinantOfMatrix() that takes matrix and its size n as input parameters and returns the determinant of the matrix.
Expected Time Complexity: O(N^{4})
Expected Auxiliary Space: O(N^{2})
Constraints:
1 <= N <= 8
-10 <= mat[i][j] <= 10
"""

def determinant_of_matrix(matrix, n):
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        ans = 0
        for col in range(n):
            small = []
            for i in range(1, n):
                dem = []
                for j in range(n):
                    if j == col:
                        continue
                    dem.append(matrix[i][j])
                small.append(dem)
            if col % 2 == 0:
                ans += matrix[0][col] * determinant_of_matrix(small, n - 1)
            else:
                ans -= matrix[0][col] * determinant_of_matrix(small, n - 1)
        return ans