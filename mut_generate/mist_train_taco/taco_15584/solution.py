"""
QUESTION:
You are given N balls numbered from 1 to N and there are N baskets numbered from 1 to N in front of you, the i^{th} basket is meant for the i^{th} ball. Calculate the number of ways in which no ball goes into its respective basket.
Example 1:
Input: N = 2
Output: 1
Explanation: The balls are numbered 1 and 2. 
Then there is only one way to dearrange them. 
The (number-basket) pairs will be [(1-2),(2-1)].
Example 2:
Input: 3
Output: 2
Explanation: The (number-basket) pairs are 
[(1-3),(2-1),(3-2)] and [(1-2),(2-3),(3-1)].
Your Task:
You do not need to read input or print anything. Your task is to complete the function disarrange() , which takes the number N as input parameter and returns the number of ways to disarrange them. As the number can be very big return it modulo 10^{9} + 7
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{4}
"""

def calculate_disarrangements(N: int) -> int:
    if N == 1:
        return 0
    if N == 2:
        return 1
    
    MOD = 10**9 + 7
    dp = [0] * N
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, N):
        dp[i] = (i * (dp[i - 1] + dp[i - 2])) % MOD
    
    return dp[N - 1]