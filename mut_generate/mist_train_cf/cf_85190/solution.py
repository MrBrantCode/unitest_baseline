"""
QUESTION:
Write a Python function `calculate_market_maker_profit` that calculates the profit made by a market maker in the options market. The function should take two parameters: `bid_price` and `ask_price`, representing the bid and ask prices of an option, respectively. The function should return the profit made by the market maker.
"""

def calculate_market_maker_profit(bid_price, ask_price):
    """
    Calculate the profit made by a market maker in the options market.
    
    Parameters:
    bid_price (float): The bid price of an option.
    ask_price (float): The ask price of an option.
    
    Returns:
    float: The profit made by the market maker.
    """
    # The profit is the difference between the ask price and the bid price
    return ask_price - bid_price