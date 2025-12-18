"""
QUESTION:
Implement a function `calculate_total_earnings` that takes an array of stock prices as input and returns the total amount of money earned from buying and selling stocks on consecutive days. The function should only include the earnings from transactions where the stock price on the selling day is higher than the stock price on the buying day. The array of stock prices contains at least two elements and all elements are positive numbers.
"""

def calculate_total_earnings(stock_prices):
    total_earnings = 0
    
    for i in range(len(stock_prices) - 1):
        if stock_prices[i+1] > stock_prices[i]:
            total_earnings += stock_prices[i+1] - stock_prices[i]
    
    return total_earnings