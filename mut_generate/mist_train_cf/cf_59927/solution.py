"""
QUESTION:
Design an algorithm for the function `maxProfitWithTransactionFee(prices, fee)` that calculates the maximum amount of profit that can be earned from an array of stock prices and a transaction fee for each trade. The function should return the maximum possible profit. The prices array and fee are the inputs to the function. The function should be efficient in terms of time and space complexity.
"""

def maxProfitWithTransactionFee(prices, fee):
    n = len(prices)
    maxProfit = [0]*n
    maxProfitAfterBuy = -prices[0]
    
    for i in range(1, n):
        maxProfit[i] = max(maxProfit[i-1], maxProfitAfterBuy + prices[i] - fee)
        maxProfitAfterBuy = max(maxProfitAfterBuy, maxProfit[i-1] - prices[i])
        
    return maxProfit[-1]