"""
QUESTION:
There are n stones and an array of heights and Geek is standing at stone 1 and can jump to one of the following: Stone i+1, i+2, ... i+k stone and cost will be [h_{i}-h_{j}] is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches Stone N.
Example 1:
Input:
n = 5, k = 3
heights = {10, 30, 40, 50, 20}
Output:
30
Explanation:
Geek will follow the path 1->2->5, the total cost 
would be | 10-30| + |30-20| = 30, which is minimum
Example 2:
Input:
n = 3, k = 1
heights = {10,20,10}
Output:
20
Explanation:
Geek will follow the path 1->2->3, the total cost
would be |10 - 20| + |20 - 10| = 20.
Your Task:
You don't need to read input or print anything. Your task is to complete the function minimizeCost() which takes the array height, and integer n, and integer k and returns the minimum energy that is lost.
Expected Time Complexity: O(n*k)
Expected Space Complexity: O(n)
Constraint:
2 <= n <= 10^{5}
1 <= k <= 100
1 <= heights[i] <= 10^{4}
"""

def minimize_cost(heights, n, k):
    dp = [-1] * n
    dp[0] = 0
    
    for ind in range(1, n):
        jumpMin = float('inf')
        for i in range(1, k + 1):
            if ind - i >= 0:
                jumpk = dp[ind - i] + abs(heights[ind - i] - heights[ind])
                jumpMin = min(jumpk, jumpMin)
        dp[ind] = jumpMin
    
    return dp[n - 1]