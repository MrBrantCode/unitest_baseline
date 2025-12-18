"""
QUESTION:
Write a function `avellaneda_k` that calculates the average number of shares traded in the market in a given time interval, representing market activity. This value is used to adjust the probability of execution in relation to market liquidity and trading volume in Avellaneda's formula for finding the probability an order gets filled. The input should include the volume of trades and the time interval.
"""

def avellaneda_k(volume, time_interval):
    """
    Calculate the average number of shares traded in the market in a given time interval.

    Args:
    volume (float): The total volume of trades.
    time_interval (float): The time interval.

    Returns:
    float: The average number of shares traded in the market in the given time interval.
    """
    return volume / time_interval