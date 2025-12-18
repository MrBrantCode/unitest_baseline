"""
QUESTION:
You are given an array prices where prices[i] is the price of a given stock on the i^{th} day, and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
Example:
Input:
n = 6
prices = [1,3,2,8,4,9]
fee = 2
Output:
8
Explanation:
The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Your Task:
You don't have to read input or print anything. Your task is to complete the function maximumProfit() which takes the integer n and array prices and transaction fee and returns the maximum profit that can earn.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
Constraint:
1 <= n <= 5*10^{4}
1 <= prices[i] < 5 * 10^{4 }
0 <= fee < 5 * 10^{4}
"""

def calculate_maximum_profit(prices, fee):
    n = len(prices)
    curr = [0, 0]
    nex = [0, 0]
    
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            if buy:
                buynow = -prices[ind] + nex[0]
                notbuy = nex[1]
                profit = max(buynow, notbuy)
            else:
                sellnow = prices[ind] + nex[1] - fee
                notsell = nex[0]
                profit = max(sellnow, notsell)
            curr[buy] = profit
        nex = curr[:]
    
    return nex[1]