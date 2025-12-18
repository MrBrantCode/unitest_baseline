"""
QUESTION:
Given a square matrix of size n×n. Your task is to calculate the sum of its diagonals.
 
Example 1:
Input: matrix = {{1, 1, 1}, 
{1, 1, 1}, {1, 1, 1}}
Output: 6
Example 2:
Input: matrix = {{1, 2}, {3, 4}}
Output: 10
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function DiagonalSum() which takes the matrix as input parameter and returns the sum of its diagonals.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
Constraints:
1 <= n <= 100
1 <= matrix elements <= 10000
"""

def calculate_diagonal_sum(matrix):
    s = 0
    n = len(matrix)
    for i in range(n):
        s += matrix[i][i]  # Add element from the primary diagonal
        if i != n - 1 - i:  # Avoid double-counting the center element in odd-sized matrices
            s += matrix[i][n - 1 - i]  # Add element from the secondary diagonal
    return s