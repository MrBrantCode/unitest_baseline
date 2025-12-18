"""
QUESTION:
Given a number N. Find the minimum number of operations required to reach N starting from 0. You have 2 operations available:
	Double the number 
	Add one to the number
Example 1:
Input:
N = 8
Output: 4
Explanation: 0 + 1 = 1, 1 + 1 = 2,
2 * 2 = 4, 4 * 2 = 8
Ã¢â¬â¹Example 2:
Input: 
N = 7
Output: 5
Explanation: 0 + 1 = 1, 1 + 1 = 2,
1 + 2 = 3, 3 * 2 = 6, 6 + 1 = 7
Your Task:
You don't need to read input or print anything. Your task is to complete the function minOperation() which accepts an integer N and return number of minimum operations required to reach N from 0.
Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{6}
"""

def min_operations_to_reach_n(N: int) -> int:
    dp = [N + 1] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        dp[i] = min(dp[i], dp[i - 1] + 1)
    
    return dp[N]