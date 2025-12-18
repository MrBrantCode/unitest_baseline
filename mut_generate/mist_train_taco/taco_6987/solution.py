"""
QUESTION:
Given a gold mine called M of (n x m) dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner can start from any row in the first column. From a given cell, the miner can move 
	to the cell diagonally up towards the right 
	to the right
	to the cell diagonally down towards the right
Find out maximum amount of gold which he can collect.
Example 1:
Input: n = 3, m = 3
M = {{1, 3, 3},
     {2, 1, 4},
     {0, 6, 4}};
Output: 12
Explaination: 
The path is {(1,0) -> (2,1) -> (2,2)}.
Example 2:
Input: n = 4, m = 4
M = {{1, 3, 1, 5},
     {2, 2, 4, 1},
     {5, 0, 2, 3},
     {0, 6, 1, 2}};
Output: 16
Explaination: 
The path is {(2,0) -> (3,1) -> (2,2) 
-> (2,3)} or {(2,0) -> (1,1) -> (1,2) 
-> (0,3)}.
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxGold() which takes the values n, m and the mine M as input parameters and returns the maximum amount of gold that can be collected.
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
Constraints:
1 ≤ n, m ≤ 50
0 ≤ M[i][j] ≤ 100
"""

def max_gold(n, m, M):
    dp = [[0 for j in range(m)] for i in range(n)]
    
    # Initialize the first column of dp with the first column of M
    for i in range(n):
        dp[i][0] = M[i][0]
    
    # Fill the dp table
    for j in range(1, m):
        for i in range(n):
            left_up = float('-inf')
            left_down = float('-inf')
            
            # Check if moving diagonally up-left is possible
            if i > 0:
                left_up = dp[i - 1][j - 1]
            
            # Check if moving diagonally down-left is possible
            if i < n - 1:
                left_down = dp[i + 1][j - 1]
            
            # Move left
            left = dp[i][j - 1]
            
            # Calculate the maximum gold that can be collected at (i, j)
            dp[i][j] = max(left, left_up, left_down) + M[i][j]
    
    # Find the maximum gold collected in the last column
    maxi = float('-inf')
    for i in range(n):
        maxi = max(maxi, dp[i][m - 1])
    
    return maxi