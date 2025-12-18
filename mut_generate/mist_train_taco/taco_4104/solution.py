"""
QUESTION:
In Geekland there is a grid of coins of size N x N. You have to find the maximum sum of coins in any sub-grid of size K x K.
Note: Coins of the negative denomination are also possible at Geekland.
Example 1:
Input: N = 5, K = 3 
mat[[]] = {1, 1, 1, 1, 1} 
          {2, 2, 2, 2, 2} 
          {3, 8, 6, 7, 3} 
          {4, 4, 4, 4, 4} 
          {5, 5, 5, 5, 5}
Output: 48
Explanation: {8, 6, 7}
             {4, 4, 4}
             {5, 5, 5}
has the maximum sum
Example 2:
Input: N = 1, K = 1
mat[[]] = {{4}} 
Output: 4
Your Task:  
You don't need to read input or print anything. Complete the function Maximum_Sum() which takes the matrix mat[], size of Matrix N, and value K as input parameters and returns the maximum sum.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
Constraints:
1 ≤ K ≤ N ≤ 10^{3}
-5*10^{5} ≤ mat[i][j] ≤ 5*10^{5}
"""

def max_sum_subgrid(mat, N, K):
    # Create a prefix sum matrix
    prefix = [[0 for _ in range(N)] for _ in range(N)]
    
    # Initialize the prefix sum matrix
    prefix[0][0] = mat[0][0]
    for i in range(1, N):
        prefix[0][i] = prefix[0][i - 1] + mat[0][i]
        prefix[i][0] = prefix[i - 1][0] + mat[i][0]
    
    # Fill the rest of the prefix sum matrix
    for i in range(1, N):
        for j in range(1, N):
            prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + mat[i][j]
    
    # Initialize the maximum sum to a very small number
    max_sum = float('-inf')
    
    # Calculate the maximum sum of any K x K sub-grid
    for i in range(K - 1, N):
        for j in range(K - 1, N):
            total = prefix[i][j]
            if i > K - 1:
                total -= prefix[i - K][j]
            if j > K - 1:
                total -= prefix[i][j - K]
            if i > K - 1 and j > K - 1:
                total += prefix[i - K][j - K]
            max_sum = max(max_sum, total)
    
    return max_sum