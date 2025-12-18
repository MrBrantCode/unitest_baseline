"""
QUESTION:
Given three integers N, M, and K and a matrix Mat of dimensions NxM. Left rotate the matrix K times.
Example 1:
Input:
N=3,M=3,K=1
Mat=[[1,2,3],[4,5,6],[7,8,9]]
Output:
2 3 1
5 6 4
8 9 7
Explanation:
Left rotating the matrix once gives this result.
Example 2:
Input:
N=3,M=3,K=2
Mat=[[1,2,3],[4,5,6],[7,8,9]]
Output:
3 1 2
6 4 5
9 7 8
Explanation:
Left rotating the matrix twice gives this result
Your Task:
You don't need to read input or print anything. Your task is to complete the function rotateMatrix() which takes the three integers N, M, K, and the matrix Mat and returns the matrix Mat left rotated K times.
Expected Time Complexity:O(N*M)
Expected Auxillary Space:O(N*M)
Constraints:
1<=N,M,Mat[i][j]<=1000
1<=K<=10000
"""

def rotate_matrix(N, M, K, matrix):
    num_rows = N
    num_cols = M
    rotated_matrix = [[0] * num_cols for _ in range(num_rows)]
    for row in range(num_rows):
        for col in range(num_cols):
            new_col = (col - K) % num_cols
            rotated_matrix[row][new_col] = matrix[row][col]
    return rotated_matrix