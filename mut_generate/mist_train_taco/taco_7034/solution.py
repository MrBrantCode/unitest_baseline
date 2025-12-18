"""
QUESTION:
Given a matrix cost of size n where cost[i][j] denotes the cost of moving from city i to city j. Your task is to complete a tour from the city 0 (0 based index) to all other cities such that you visit each city atmost once and then at the end come back to city 0 in min cost.
 
Example 1:
Input: cost = {{0,111},{112,0}}
Output: 223
Explanation: We can visit 0->1->0 and 
cost = 111 + 112.
Example 2:
Input: cost = {{0,1000,5000},{5000,0,1000},
{1000,5000,0}}
Output: 3000
Explanation: We can visit 0->1->2->0 and cost 
= 1000+1000+1000 = 3000
 
Your Task:
You don't need to read or print anything. Your task is to complete the function total_cost() which takes cost as input parameter and returns the total cost to visit each city exactly once starting from city 0 and again comback to city 0.
 
Expected Time Complexity: O(2^{n} * n^{2})
Expected Space Compelxity: O(2^{n} * n)
 
Constraints:
1 <= n <= 20
1 <= cost[i][j] <= 10^{3}
"""

def calculate_min_tour_cost(cost):
    n = len(cost)
    if n == 1:
        return 0
    
    dp = [[-1 for _ in range(1 << n)] for _ in range(n)]
    
    def solve(state, city):
        if state == 0:
            return cost[city][0]
        if dp[city][state] != -1:
            return dp[city][state]
        cst = float('inf')
        for i in range(n):
            if state & (1 << i):
                cst = min(cst, cost[city][i] + solve(state ^ (1 << i), i))
        dp[city][state] = cst
        return cst
    
    return solve((1 << n) - 2, 0)