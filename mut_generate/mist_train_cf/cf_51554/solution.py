"""
QUESTION:
Estimate cancellation statistics from Level of Book (LOB) snapshots.

Create a function `estimate_cancellations` that estimates cancellation statistics (total cancelled volume and average prices) from LOB snapshots. Each snapshot includes top 10-level bid/ask price/volume, cumulative volume, turnover, OHLC, and last traded price. The snapshots are generated per second.
"""

def estimate_cancellations(snapshots):
    """
    Estimate cancellation statistics from LOB snapshots.

    Parameters:
    snapshots (list): A list of LOB snapshots.

    Returns:
    dict: Estimated cancellation statistics (total cancelled volume and average prices).
    """
    # Initialize variables to store total cancelled volume and average prices
    total_cancelled_volume = 0
    total_cancelled_value = 0
    
    # Iterate through each snapshot
    for i in range(1, len(snapshots)):
        # Calculate changes in bid and ask volume
        bid_volume_change = snapshots[i]['bid_volume'] - snapshots[i-1]['bid_volume']
        ask_volume_change = snapshots[i]['ask_volume'] - snapshots[i-1]['ask_volume']
        
        # Assume changes in volume are due to cancellations
        cancelled_volume = abs(bid_volume_change) + abs(ask_volume_change)
        
        # Update total cancelled volume
        total_cancelled_volume += cancelled_volume
        
        # Calculate average price of cancelled orders
        if cancelled_volume > 0:
            average_price = (snapshots[i]['last_traded_price'] + snapshots[i-1]['last_traded_price']) / 2
            total_cancelled_value += cancelled_volume * average_price
    
    # Calculate average price of all cancelled orders
    if total_cancelled_volume > 0:
        average_price = total_cancelled_value / total_cancelled_volume
    else:
        average_price = 0
    
    # Return estimated cancellation statistics
    return {
        'total_cancelled_volume': total_cancelled_volume,
        'average_price': average_price
    }