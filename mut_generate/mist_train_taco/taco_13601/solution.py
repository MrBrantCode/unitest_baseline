"""
QUESTION:
There is a 2D matrix of N rows and M columns. Rows are number 1 to N from top to bottom and columns 1 to M from left to right. You are standing at (1,1).   

From, A [ i ] [ j ] you can move to A [ i + 1 ] [ j ] if A [ i + 1 ] [ j ] > A [ i ] [ j ].
Or, from, A [ i ] [ j ] you can move to A [ i ] [ j + 1 ] if A [ i ] [ j + 1 ] > A [ i ] [ j ].

Moving from (1,1), what is the longest path that you can travel?

Input: 
First line contains, T, the number of testcases. Each testcase consists of N, M. Each of the next N lines contain M integers each.

Output: 
For each testcase, print the length of the longest path from (1,1).

Constraints: 
1 ≤ T ≤ 100 
1 ≤ N, M ≤ 100 
1 ≤ A[i][j] ≤ 10^6

SAMPLE INPUT
3
1 1
1
4 4
1 2 3 4
2 2 3 4
3 2 3 4
4 5 6 7
2 2
1 2
3 4

SAMPLE OUTPUT
1
7
3

Explanation

In first testcase the path is of 1 length only i.e. (1,1).
In second testcase, the path of length 7 is (1,1) , (2,1), (3,1), (4,1), (4,2), (4,3), (4,4).
In third case, any of the following paths can be taken.
(1,1), (1,2), (2,2) or (1,1), (1,2), (2,2). Both are of length 3.
"""

def find_longest_path_length(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    n = len(matrix)
    m = len(matrix[0])
    
    # Initialize the path matrix with zeros
    path_matrix = [[0] * m for _ in range(n)]
    
    # Starting point (1,1) in 0-indexed is (0,0)
    path_matrix[0][0] = 1
    
    # Fill the path matrix
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i > 0 and matrix[i][j] > matrix[i-1][j] and path_matrix[i-1][j] != 0:
                path_matrix[i][j] = path_matrix[i-1][j] + 1
            if j > 0 and matrix[i][j] > matrix[i][j-1] and path_matrix[i][j-1] != 0:
                path_matrix[i][j] = max(path_matrix[i][j], path_matrix[i][j-1] + 1)
    
    # Find the maximum value in the path matrix
    max_path_length = max(max(row) for row in path_matrix)
    
    return max_path_length