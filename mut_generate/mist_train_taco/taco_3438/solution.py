"""
QUESTION:
Given N, count the number of ways to express N as sum of 1, 3 and 4 modulo (10^{9}+7).
 
Example 1:  
Input:
N = 1
Output:
1
Explanation:
There is only one way to represent 1 as
sum of 1,3 and 4. 1 = {1}.
Example 2:  
Input:
N = 3
Output:
2
Explanation:
There is 2 ways to represent 3 as sum
of 1,3 and 4. 3 = {1,1,1}, and 3 = {3}.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function countWays() which takes a Integer N as input and returns the number of ways possible.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{5}
"""

def count_ways_to_express_sum(N: int) -> int:
    mod = 10**9 + 7
    
    if N <= 2:
        return 1
    
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    
    for i in range(4, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 3] + dp[i - 4]) % mod
    
    return dp[N]