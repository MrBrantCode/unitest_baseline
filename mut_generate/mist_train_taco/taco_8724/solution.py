"""
QUESTION:
For 2 given matrices of size n x n. Your task is to multiply them.
 
Example 1:Ã¢â¬â¹
Ã¢â¬â¹Input: 
matrixA = {{1, 1, 1}, {1, 1, 1}, 
           {1, 1, 1}}
matrixB = {{1, 1, 1}, {1, 1, 1},
           {1, 1, 1}}
Output: {{3, 3, 3}, {3, 3, 3}, {3, 3, 3}}
Example 2:
Input: 
matrixA = {{1, 2}, {3, 4}},
matrixB = {{4, 3}, {2, 1}}
Output: {{8, 5}, {20, 13}}
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Multiply() which takes two matrices matrixA amd matrixB as input parameter and multiply the two matrices. You don't have to return anything. Copy the values of output matrix into matrixA.
 
Expected Time Compelxity: O(n^{3})
Expected Space Complexity: O(n^{2})
 
Constraints:
1 <= n <= 100
1 <= elements of matrices <= 100
"""

def matrix_multiply(matrixA, matrixB):
    n = len(matrixA)
    matrixC = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ans = 0
            for k in range(n):
                ans += matrixA[i][k] * matrixB[k][j]
            matrixC[i][j] = ans
    
    return matrixC