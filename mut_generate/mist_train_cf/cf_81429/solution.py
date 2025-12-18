"""
QUESTION:
Create two functions, `four_times_leverage_put_options` and `four_times_leverage_synthetic_short_stock`, to devise and customize a 4 times leverage on a stock price downward movement. The functions should take into account a 1-year holding period and the possibility of rolling options.

Implement `four_times_leverage_put_options` using put options to achieve a 4 times leverage. The function should consider buying put options on the stock with a specified strike price and an expiration date 1 year from now.

Implement `four_times_leverage_synthetic_short_stock` using a synthetic short stock strategy. The function should consider buying 4 put options and selling 4 call options on the stock with the same strike price and expiration date to mimic short selling a stock.

Both functions should be able to roll the options to maintain the position for a year.
"""

def four_times_leverage_put_options(strike_price, stock_price):
    """
    This function devises a 4 times leverage on a stock price downward movement 
    using put options.

    Parameters:
    strike_price (float): The price at which the option can be exercised.
    stock_price (float): The current price of the stock.

    Returns:
    float: The profit from the put options.
    """
    # Calculate the profit from the put options
    profit = 4 * (strike_price - stock_price)
    return profit


def four_times_leverage_synthetic_short_stock(strike_price, stock_price):
    """
    This function devises a 4 times leverage on a stock price downward movement 
    using a synthetic short stock strategy.

    Parameters:
    strike_price (float): The price at which the option can be exercised.
    stock_price (float): The current price of the stock.

    Returns:
    float: The profit from the synthetic short stock strategy.
    """
    # Calculate the profit from the synthetic short stock strategy
    # This is a simplified calculation and does not take into account 
    # other factors that can affect the profit, such as time decay and volatility.
    profit = 4 * (strike_price - stock_price)
    return profit