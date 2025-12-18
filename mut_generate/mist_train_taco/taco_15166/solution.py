"""
QUESTION:
Given a binary matrix mat[][] of dimensions NxM such that 1 denotes land and 0 denotes water. Find the number of closed islands in the given matrix. 
Note: A closed island is a group of 1s surrounded by only 0s on all the boundaries (except diagonals). In simple words, a closed island is an island whose none of the 1s lie on the edges of the matrix.
Example 1:
Input:
N = 5, M = 8
mat[][] = {{0, 0, 0, 0, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 0, 1}, 
           {0, 1, 0, 1, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 1, 0}, 
           {1, 0, 0, 0, 0, 1, 0, 1}}
Output:
2
Explanation:
mat[][] = {{0, 0, 0, 0, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 0, 1}, 
           {0, 1, 0, 1, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 1, 0}, 
           {1, 0, 0, 0, 0, 1, 0, 1}} 
There are 2 closed islands. The islands in dark are closed because they are completely surrounded by 0s (water). There are two more islands in the last column of the matrix, but they are not completely surrounded by 0s. Hence they are not closed islands. 
Example 2:
Input:
N = 3, M = 3
mat[][] = {{1, 0, 0},
           {0, 1, 0},
           {0, 0, 1}}
Output: 
1
Explanation:
mat[][] = {{1, 0, 0},
          {0, 1, 0},
          {0, 0, 1}}
There is just a one closed island.
Your task:
You dont need to read input or print anything. Your task is to complete the function closedIslands() which takes two integers N and M, and a 2D binary matrix mat as input parameters and returns the number of closed islands.
Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)
Constraints:
1 ≤ N,M ≤ 500
"""

def count_closed_islands(matrix, N, M):
    def dfs(matrix, N, M, i, j):
        matrix[i][j] = 0
        if i in (0, N - 1) or j in (0, M - 1):
            return False
        flag1 = True
        flag2 = True
        flag3 = True
        flag4 = True
        if i >= 1 and matrix[i - 1][j]:
            flag1 = dfs(matrix, N, M, i - 1, j)
        if i <= N - 1 and matrix[i + 1][j]:
            flag2 = dfs(matrix, N, M, i + 1, j)
        if j >= 1 and matrix[i][j - 1]:
            flag3 = dfs(matrix, N, M, i, j - 1)
        if j <= M - 1 and matrix[i][j + 1]:
            flag4 = dfs(matrix, N, M, i, j + 1)
        return flag1 and flag2 and flag3 and flag4

    count = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if matrix[i][j] == 1 and dfs(matrix, N, M, i, j):
                count += 1
    return count