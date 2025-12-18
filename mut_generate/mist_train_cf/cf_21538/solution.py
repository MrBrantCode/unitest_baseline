"""
QUESTION:
Design a function `calculateMaxProfit(sharePrices)` that calculates the maximum profit for buying/selling any number of shares of a company's stock with a maximum of two transactions. The function should take a list of share prices as input and return the maximum possible profit. The function should have a time complexity of O(n) and space complexity of O(1), where n is the number of share prices.
"""

def calculateMaxProfit(sharePrices):
    buy1 = float('-inf')
    sell1 = 0
    buy2 = float('-inf')
    sell2 = 0

    for price in sharePrices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, price + buy1)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, price + buy2)

    return sell2