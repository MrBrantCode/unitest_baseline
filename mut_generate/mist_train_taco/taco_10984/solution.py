"""
QUESTION:
You are given the prices of stock for n number of days. every ith day tell the price of the stock on that day. find the maximum profit that you can make by buying and selling stock with the restriction of  After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Example:
Input:
5
1 2 3 0 2
Output:
3
Explanation:
You buy on 1st day and sell on the second day then cooldown, then buy on the fourth day and
sell on the fifth day and earn a profit of 3.
Your Task:
You don't have to read input or print anything. Your task is to complete the function maximumProfit() which takes the integer n and array prices and returns the maximum profit that can earn.
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
Constraint:
1<=n<=10^{5}
1<=prices[i]<=10^{5}
"""

def maximum_profit(prices):
    n = len(prices)
    if n == 0:
        return 0
    
    dp = [[0 for _ in range(2)] for _ in range(n + 2)]
    
    for i in range(n - 1, -1, -1):
        for j in range(2):
            profit = 0
            if j:
                profit = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
            else:
                profit = max(prices[i] + dp[i + 2][1], 0 + dp[i + 1][0])
            dp[i][j] = profit
    
    return dp[0][1]