"""
QUESTION:
Implement the `save_to_non_existing_column` function to save the given stock price data to a specified column in a 2D NumPy array. If the specified column does not exist in the array, add the column to the array and then save the stock price data. The function should take three parameters: a 2D NumPy array representing stock data, the index of the column to save the stock prices to, and a 1D NumPy array containing stock price data. The function should return the updated 2D NumPy array with stock price data saved to the specified column. The stock price data array may have fewer rows than the stock data array, in which case the function should pad the stock price data array with zeros before saving it to the stock data array.
"""

import numpy as np

def save_to_non_existing_column(stock, column_index, stock_prices):
    """
    Saves the stock price data to the specified column in a 2D NumPy array representing stock data.
    
    Args:
    stock: 2D NumPy array representing stock data
    column_index: Index of the column to save the stock prices to
    stock_prices: 1D NumPy array containing stock price data
    
    Returns:
    Updated 2D NumPy array with stock price data saved to the specified column
    """
    num_rows = stock.shape[0]
    num_cols = stock.shape[1]
    
    if column_index >= num_cols:
        # Add new column to the array
        new_column = np.zeros((num_rows, column_index - num_cols + 1))
        stock = np.hstack((stock, new_column))
    
    stock[:, column_index] = np.pad(stock_prices, (0, num_rows - len(stock_prices)), 'constant')
    return stock