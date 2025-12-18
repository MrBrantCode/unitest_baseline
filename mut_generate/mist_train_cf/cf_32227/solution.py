"""
QUESTION:
Create a function `max_profit` that takes a list of stock tickers, where each ticker is a tuple containing the ticker symbol and a list of stock prices over time. The function should return the maximum profit achievable by buying and selling one share of any stock, with the condition that the buying and selling prices must be on different days and the selling price must be higher than the buying price. The function should not consider the ticker symbol, only the list of stock prices. The maximum profit should be a float value.
"""

from typing import List, Tuple

def max_profit(tickers: List[Tuple[str, List[float]]]) -> float:
    max_profit = 0.0
    for _, prices in tickers:
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
    return max_profit