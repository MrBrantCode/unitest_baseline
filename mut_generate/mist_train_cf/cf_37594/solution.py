"""
QUESTION:
Implement the function `average_trade_volume(trades, start_time, end_time)` that calculates the average trade volume for a given cryptocurrency pair within a specified time range. The function takes in a list of dictionaries `trades` where each dictionary represents a trade with keys "timestamp" (datetime object), "volume" (float), and "count" (integer), and two datetime objects `start_time` and `end_time` representing the start and end of the time range. Return the average trade volume rounded to 8 decimal places.
"""

from datetime import datetime

def average_trade_volume(trades, start_time, end_time) -> float:
    total_volume = 0
    trade_count = 0

    for trade in trades:
        if start_time <= trade["timestamp"] <= end_time:
            total_volume += trade["volume"]
            trade_count += 1

    if trade_count == 0:
        return 0.0  

    average_volume = total_volume / trade_count
    return round(average_volume, 8)