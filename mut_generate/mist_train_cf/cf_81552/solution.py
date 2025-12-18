"""
QUESTION:
Write a function named `mdtv_alternative` to compute an alternative MDTV (Median Daily Traded Value) liquidity for options. The function should take in a list of traded volumes for the past 90 days. Assume that the input list contains at least 90 elements and the volumes are non-negative.
"""

def mdtv_alternative(traded_volumes):
    """
    Compute an alternative MDTV (Median Daily Traded Value) liquidity for options.

    Args:
    traded_volumes (list): A list of traded volumes for the past 90 days.

    Returns:
    float: The alternative MDTV for options.
    """
    # Calculate the volume over a longer period (365 days in this example)
    traded_volumes_longer_period = traded_volumes[-365:]

    # Calculate the median of the traded volumes
    median_volume = sorted(traded_volumes_longer_period)[len(traded_volumes_longer_period) // 2]

    # Apply a weighted average (more recent trading days carry more weight)
    weighted_sum = sum(i * volume for i, volume in enumerate(traded_volumes_longer_period, start=1))
    weighted_average = weighted_sum / sum(range(1, len(traded_volumes_longer_period) + 1))

    # Apply liquidity adjustments (in this example, a simple adjustment based on bid-ask spread)
    # For simplicity, assume bid_ask_spread is given
    bid_ask_spread = 0.01  # Replace with actual bid-ask spread
    liquidity_adjustment = 1 / (1 + bid_ask_spread)

    # Calculate the alternative MDTV
    alternative_mdtv = weighted_average * liquidity_adjustment

    return alternative_mdtv