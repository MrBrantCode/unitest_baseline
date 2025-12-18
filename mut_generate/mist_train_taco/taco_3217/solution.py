"""
QUESTION:
Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins_{1}, coins_{2}, ..., coins_{m}} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.
Example 1:
Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin
and one 5 cent coin
Example 2:
Input: V = 11, M = 4,coins[] = {9, 6, 5, 1} 
Output: 2 
Explanation: Use one 6 cent coin
and one 5 cent coin
Your Task:  
You don't need to read input or print anything. Complete the function minCoins() which takes V, M and array coins as input parameters and returns the answer.
Expected Time Complexity: O(V*M)
Expected Auxiliary Space: O(V)
Constraints:
1 ≤ V*M ≤ 10^{6}
All array elements are distinct
"""

def min_coins(V: int, coins: list) -> int:
    n = len(coins)
    dp = [[float('inf') for _ in range(V + 1)] for _ in range(n + 1)]
    
    # Base case: 0 coins needed to make 0 value
    for i in range(n + 1):
        dp[i][0] = 0
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, V + 1):
            if j < coins[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
    
    return dp[n][V] if dp[n][V] != float('inf') else -1