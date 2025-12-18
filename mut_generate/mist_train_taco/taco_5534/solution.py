"""
QUESTION:
You are given a rectangular grid with n rows and m columns. The rows are numbered 1 to n, from bottom to top, and the columns are numbered 1 to m, from left to right.   

You are also given k special fields in the form (row, column). For each i, where 0 ≤ i ≤ k, count the number of different paths from (1, 1) to (n, m) that contains exactly n special fields.  

There is one rule you must follow. You are only allowed to make moves that are straight up or to the right. In other words, from each field (row, column), you can only move to field (row+1, column) or field (row, column+1).  

Output an array of k + 1 elements. The i-th element (0-indexed) must be the number of different paths that contain exactly i special fields. Since, the answer can be too big, output it modulo 1000007.  

Input: 
First line contains three space separated integers, n, m and k.
Next k lines, each contain two space separated integers, the coordinates of a special field.

Output:
k + 1 space separated integers, the answer to the question.  

Constraints:
1 ≤ n, m, k ≤ 100
For all coordinates (r, c) - 1 ≤ r ≤ n, 1 ≤ c ≤ m
All coordinates are valid and different.    

SAMPLE INPUT
3 3 2
2 2
3 2

SAMPLE OUTPUT
1 3 2

Explanation

0 special cell -
    (1, 1) -> (1, 2) -> (1, 3) -> (2, 3) -> (3, 3)  

1 special cell -
    (1, 1) -> (2, 1) -> (2, 2) -> (2, 3) -> (3, 3)
    (1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (3, 3)
    (1, 1) -> (1, 2) -> (2, 2) -> (2, 3) -> (3, 3)  

2 special cells -
    (1, 1) -> (2, 1) -> (2, 2) -> (3, 2) -> (3, 3)
    (1, 1) -> (1, 2) -> (2, 2) -> (3, 2) -> (3, 3)
"""

def count_paths_with_special_fields(n, m, k, special_fields):
    MOD = 1000007
    
    # Initialize the special grid
    special = [[False for _ in range(m)] for _ in range(n)]
    for (r, c) in special_fields:
        special[r - 1][c - 1] = True
    
    # Initialize the DP table
    dp = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    
    # Base cases for the first row
    for k_val in range(k + 1):
        special_count = 0
        for j in range(m):
            if special[0][j]:
                special_count += 1
            if special_count <= k_val:
                dp[0][j][k_val] = 1
    
    # Base cases for the first column
    for k_val in range(k + 1):
        special_count = 0
        for i in range(n):
            if special[i][0]:
                special_count += 1
            if special_count <= k_val:
                dp[i][0][k_val] = 1
    
    # Fill the DP table
    for i in range(1, n):
        for j in range(1, m):
            for k_val in range(k + 1):
                if not special[i][j]:
                    dp[i][j][k_val] = (dp[i - 1][j][k_val] + dp[i][j - 1][k_val]) % MOD
                elif k_val > 0:
                    dp[i][j][k_val] = (dp[i - 1][j][k_val - 1] + dp[i][j - 1][k_val - 1]) % MOD
    
    # Calculate the final answer
    ans = [0] * (k + 1)
    ans[0] = dp[n - 1][m - 1][0]
    for k_val in range(1, k + 1):
        ans[k_val] = (dp[n - 1][m - 1][k_val] - dp[n - 1][m - 1][k_val - 1]) % MOD
    
    return ans