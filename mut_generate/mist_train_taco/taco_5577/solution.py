"""
QUESTION:
Given a matrix M of size n * n, the task is to find sum of the zigzag sequence with the largest sum. A zigzag sequence starts from the top and ends at the bottom. Two consecutive elements of sequence cannot belong to same column.
Example 1:
Input: n = 3
M = {{3, 1, 2}, 
     {4, 8, 5}, 
     {6, 9, 7}}
Output: 18
Explaination: The sequence is (3, 8, 7).
Example 2:
Input: n = 3
M = {{1, 2, 4}, 
     {3, 9, 6}, 
     {11, 3, 15}}
Output: 28
Explaination: The sequence is 4, 9, 15.
Your Task:
You do not need to read input or print anything. Your task is to complete the function zigzagSequence() which takes n and M as input parameters and returns the highest zigzag sum.
Expected Time Complexity: O(n^{3})
Expected Auxiliary Space: O(n^{2})  
Constraints:
1 ≤ n ≤ 100
1 ≤ M[i][j] ≤ 1000
"""

def find_max_zigzag_sum(n, M):
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == 0:
                dp[i][j] = M[i][j]
            else:
                for k in range(n):
                    if k != j:
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + M[i][j])
    
    return max(dp[n - 1])