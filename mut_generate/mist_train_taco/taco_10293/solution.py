"""
QUESTION:
Given a fence with n posts and k colors, find out the number of ways of painting the fence so that not more than two consecutive posts have the same colors. Since the answer can be large return it modulo 10^9 + 7.
Example 1:
Input:
N=3,  K=2 
Output: 6
Explanation: 
We have following possible combinations:
 
Example 2:
Input:
N=2,  K=4
Output: 16
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function countWays() that takes n and k as parameters and returns the number of ways in which the fence can be painted.(modulo 10^{9} + 7)
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 5000
1 ≤ K ≤ 100
"""

def count_painting_ways(n: int, k: int) -> int:
    MOD = 10**9 + 7
    
    if n == 0:
        return 0
    if n == 1:
        return k
    
    dp = [[0, 0] for _ in range(n)]
    dp[0] = [k, 0]
    
    for i in range(1, n):
        dp[i][0] = (dp[i - 1][0] * (k - 1) + dp[i - 1][1] * (k - 1)) % MOD
        dp[i][1] = dp[i - 1][0]
    
    return sum(dp[n - 1]) % MOD