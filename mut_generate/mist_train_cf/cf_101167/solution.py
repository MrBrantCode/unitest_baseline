"""
QUESTION:
Calculate the average price for each stock and determine the highest and lowest performing stocks based on their average prices in descending order. The function should also calculate the percentage increase or decrease of each stock's performance compared to the overall market performance. The input is a dictionary where the keys are the stock symbols and the values are lists of prices for each stock. The output should be two lists of tuples, one for the highest performing stocks and one for the lowest performing stocks, where each tuple contains the stock symbol and its average price, and the percentage increase or decrease in performance.
"""

def stock_performance(stocks):
    # calculate average prices for each stock
    averages = {stock: sum(prices) / len(prices) for stock, prices in stocks.items()}
    
    # determine highest and lowest performing stocks based on average prices
    high_performers = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    low_performers = sorted(averages.items(), key=lambda x: x[1])
    
    # calculate percentage increase/decrease compared to overall market performance
    market_average = sum(averages.values()) / len(averages)
    percentages = {stock: ((avg_price - market_average) / market_average) * 100 for stock, avg_price in averages.items()}
    
    # return results
    return high_performers, low_performers, percentages