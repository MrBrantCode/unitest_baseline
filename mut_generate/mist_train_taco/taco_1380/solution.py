"""
QUESTION:
Given an array cost[] of positive integers of size N and an integer W, cost[i] represents the cost of i kg packet of oranges, the task is to find the minimum cost to buy W kgs of oranges. If it is not possible to buy exactly W kg oranges then the output will be -1
Note:
1. cost[i] = -1 means that i kg packet of orange is unavailable
2.  It may be assumed that there is infinite supply of all available packet types.
Example 1:
Input: N = 5, arr[] = {20, 10, 4, 50, 100}
W = 5
Output: 14
Explanation: choose two oranges to minimize 
cost. First orange of 2Kg and cost 10. 
Second orange of 3Kg and cost 4. 
Example 2:
Input: N = 5, arr[] = {-1, -1, 4, 3, -1}
W = 5
Output: -1
Explanation: It is not possible to buy 5 
kgs of oranges
Your Task:  
You don't need to read input or print anything. Complete the function minimumCost() which takes N, W, and array cost as input parameters and returns the minimum value.
Expected Time Complexity: O(N*W)
Expected Auxiliary Space: O(N*W)
Constraints:
1 ≤ N, W ≤ 2*10^{2}
-1 ≤ cost[i] ≤ 10^{5}
cost[i] ≠ 0
"""

def minimum_cost(cost, N, W):
    def go(ind, currw):
        if currw > W:
            return 10 ** 18
        if ind == N:
            if currw == W:
                return 0
            return 10 ** 18
        if dp[ind][currw] != -1:
            return dp[ind][currw]
        c1 = 10 ** 18
        if cost[ind] != -1:
            c1 = cost[ind] + go(ind, currw + ind + 1)
        c2 = go(ind + 1, currw)
        ans = min(c1, c2)
        dp[ind][currw] = ans
        return ans
    
    dp = [[-1] * (W + 1) for _ in range(N)]
    ans1 = go(0, 0)
    if ans1 == 10 ** 18:
        return -1
    return ans1