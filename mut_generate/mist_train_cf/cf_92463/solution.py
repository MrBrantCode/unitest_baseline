"""
QUESTION:
Implement a function `calculate_total_earnings` that calculates the total earnings from buying and selling stocks on consecutive days given an array of stock prices. The function should only consider stock prices where the selling price is higher than the buying price. The input array will contain at least two elements.
"""

def calculate_total_earnings(stock_prices):
    total_earnings = 0
    
    for i in range(len(stock_prices) - 1):
        if stock_prices[i+1] > stock_prices[i]:
            total_earnings += stock_prices[i+1] - stock_prices[i]
    
    return total_earnings