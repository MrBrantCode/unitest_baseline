"""
QUESTION:
Given OHLCV (Open, High, Low, Close, and Volume) data, write a function `calculate_volume_profile` to approximate the volume profile by distributing the volume among price levels between the low and high. Use the two approximation methods: Simplest approximation and VWAP (Volume Weighted Average Price) approximation.
"""

import numpy as np

def calculate_volume_profile(high, low, close, volume):
    """
    Approximate the volume profile by distributing the volume among price levels between the low and high.

    Args:
        high (float): The highest price in the interval.
        low (float): The lowest price in the interval.
        close (float): The closing price of the interval.
        volume (float): The total volume traded in the interval.

    Returns:
        A dictionary containing the approximated volume profiles using Simplest and VWAP approximations.
    """

    # Calculate the number of price levels
    price_levels = np.arange(low, high + 1)

    # Simplest approximation: Assume the volume is distributed evenly among all price levels
    simplest_approximation = {price: volume / len(price_levels) for price in price_levels}

    # VWAP (Volume Weighted Average Price) approximation
    vwap_approximation = {price: volume * (close - low) / (high - low) / len(price_levels) for price in price_levels}

    return {
        "Simplest Approximation": simplest_approximation,
        "VWAP Approximation": vwap_approximation
    }