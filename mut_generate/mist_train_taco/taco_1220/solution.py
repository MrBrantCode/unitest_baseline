"""
QUESTION:
Given a number N, the task is to count minimum steps to minimize it to 1 according to the following criteria:
	If N is divisible by 2 then you may reduce N to N/2.
	If N is divisible by 3 then you may reduce N to N/3.
	Otherwise, Decrement N by 1.
Example 1:
Input: N = 10
Output: 3
Explanation: 10 - 1 = 9 / 3 = 3 / 3 = 1
Example 2:
Input: N = 1
Output: 0
Explanation: N is 1
Your Task:  
You don't need to read input or print anything. Complete the function minSteps() which takes N as input parameters and returns the integer value
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{4}
"""

def min_steps_to_one(N: int) -> int:
    MAX = 100000
    dp = [-1 for _ in range(N + 1)]
    dp[1] = 0
    
    for i in range(2, N + 1):
        dp[i] = 1 + min(
            dp[i - 1],
            dp[i // 2] if i % 2 == 0 else MAX,
            dp[i // 3] if i % 3 == 0 else MAX
        )
    
    return dp[N]