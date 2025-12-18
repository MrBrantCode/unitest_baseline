"""
QUESTION:
Implement the function `calculateMovingAverages(stock, K_short, K_long)` that takes in a pandas DataFrame `stock` containing a 'Close' column for a stock's closing prices and the constants `K_short` and `K_long` representing the smoothing factors for the short-term and long-term moving averages. The function should update the 'MovAvgShort', 'MovAvgLong', and 'MovAvgDiff' columns in the DataFrame according to the moving average formulas: 
- MA_short = (K_short * close) + (1 - K_short) * last_close
- MA_long = (K_long * close) + (1 - K_long) * last_close
- MovAvgDiff = MovAvgShort - MovAvgLong
The function should return the updated DataFrame with moving averages and differences rounded to 4 decimal places.
"""

import pandas as pd

def calculateMovingAverages(stock: pd.DataFrame, K_short: float, K_long: float) -> pd.DataFrame:
    last_close = stock.at[0, "Close"]
    stock.at[0, "MovAvgShort"] = round((K_short * last_close) + (1 - K_short) * last_close, 4)
    stock.at[0, "MovAvgLong"] = round((K_long * last_close) + (1 - K_long) * last_close, 4)
    stock.at[0, "MovAvgDiff"] = round(stock.at[0, "MovAvgShort"] - stock.at[0, "MovAvgLong"], 4)

    for idx, curr in stock.iterrows():
        if idx == 0:
            continue
        close = curr["Close"]
        stock.at[idx, "MovAvgShort"] = round((K_short * close) + (1 - K_short) * last_close, 4)
        stock.at[idx, "MovAvgLong"] = round((K_long * close) + (1 - K_long) * last_close, 4)
        stock.at[idx, "MovAvgDiff"] = round(stock.at[idx, "MovAvgShort"] - stock.at[idx, "MovAvgLong"], 4)
        last_close = close

    return stock