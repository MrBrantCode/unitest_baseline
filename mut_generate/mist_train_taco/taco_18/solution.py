"""
QUESTION:
You are given the prices of stock for n number of days. every ith day tell the price of the stock on that day.find the maximum profit that you can make by buying and selling stock any number of times as you can't proceed with other transactions if you hold any transaction.
Example:
Input:
n = 7
prices = [1,2,3,4,5,6,7]
Output:
6
Explaination:
We can make the maximum profit by buying the stock on the first day and selling it on the last day.
Your Task:
You don't have to read input or print anything. Your task is to complete the function maximizeProfit() which takes the integer n and array prices and returns the maximum profit that can earn.
Expected Time Complexity: O(n)
Expected Space Complexity: O(n^{2})
NOTE: can you solve this in less space complexity?
Constraint:
1<=n<=10^{5}
1<=prices[i]<=10^{5}
"""

def maximize_profit(prices, n):
    if n == 0:
        return 0
    
    curr = [0, 0]
    nex = [0, 0]
    
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            if buy:
                buynow = -prices[ind] + nex[0]
                notbuy = nex[1]
                profit = max(buynow, notbuy)
            else:
                sellnow = prices[ind] + nex[1]
                notsell = nex[0]
                profit = max(sellnow, notsell)
            curr[buy] = profit
        nex = curr[:]
    
    return nex[1]