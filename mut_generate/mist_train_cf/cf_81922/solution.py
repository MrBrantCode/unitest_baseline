"""
QUESTION:
Create a function called `calculate_slippage` that takes in parameters such as order size, currency pair, time of day, and average trading volume. Approximate the quote deviation (slippage) induced by the opening or closing of an order in a Forex simulator, assuming a highly liquid market and considering factors such as liquidity conditions and trading volume.
"""

def calculate_slippage(order_size, currency_pair, time_of_day, average_trading_volume):
    """
    Approximate the quote deviation (slippage) induced by the opening or closing of an order in a Forex simulator.

    Parameters:
    order_size (float): The size of the order.
    currency_pair (str): The currency pair being traded.
    time_of_day (str): The time of day the order is being placed.
    average_trading_volume (float): The average trading volume for the currency pair.

    Returns:
    float: The approximate slippage.
    """

    # Assuming a base slippage for the most liquid currency pair (EUR/USD) during normal market hours
    base_slippage = 0.0001

    # Adjusting the base slippage based on the currency pair
    if currency_pair == 'EUR/USD':
        pair_slippage = base_slippage
    elif currency_pair == 'USD/JPY':
        pair_slippage = base_slippage * 1.2
    else:
        pair_slippage = base_slippage * 1.5

    # Adjusting the slippage based on the time of day
    if time_of_day == 'market_open' or time_of_day == 'market_close':
        time_slippage = pair_slippage * 1.5
    else:
        time_slippage = pair_slippage

    # Adjusting the slippage based on the order size relative to the average trading volume
    volume_slippage = time_slippage * (order_size / average_trading_volume)

    return volume_slippage