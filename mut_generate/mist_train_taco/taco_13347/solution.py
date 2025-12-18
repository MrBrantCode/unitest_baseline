"""
QUESTION:
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top (order does matter).
Example 1:
Input:
n = 4
Output: 5
Explanation:
You can reach 4th stair in 5 ways. 
Way 1: Climb 2 stairs at a time. 
Way 2: Climb 1 stair at a time.
Way 3: Climb 2 stairs, then 1 stair
and then 1 stair.
Way 4: Climb 1 stair, then 2 stairs
then 1 stair.
Way 5: Climb 1 stair, then 1 stair and
then 2 stairs.
Example 2:
Input:
n = 10
Output: 89 
Explanation: 
There are 89 ways to reach the 10th stair.
Your Task:
Complete the function countWays() which takes the top stair number m as input parameters and returns the answer % 10^9+7.
Expected Time Complexity : O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 10^{4}
"""

def count_ways_to_climb_stairs(n: int) -> int:
    MOD = 10**9 + 7
    
    # Base cases
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    # Initialize the DP array
    dp = [-1] * (n + 1)
    
    def helper(n, dp):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        
        one_step = helper(n - 1, dp)
        two_step = helper(n - 2, dp)
        dp[n] = (one_step + two_step) % MOD
        return dp[n]
    
    return helper(n, dp)