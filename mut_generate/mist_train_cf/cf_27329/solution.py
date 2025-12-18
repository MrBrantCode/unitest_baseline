"""
QUESTION:
Write a function `calculate_adosc(df)` that takes a pandas DataFrame `df` as input, containing columns 'high', 'low', 'close', and 'volume', and returns a pandas Series of Accumulation/Distribution Oscillator (ADOSC) values. The ADOSC is calculated as the 14-period moving average of the product of the volume and the difference between the close-low and high-close, divided by the high-low range.
"""

import pandas as pd

def calculate_adosc(df):
    high = df['high']
    low = df['low']
    close = df['close']
    volume = df['volume']

    ad = ((close - low) - (high - close)) / (high - low)
    adosc = ad * volume
    adosc = adosc.rolling(window=14).mean()

    return adosc