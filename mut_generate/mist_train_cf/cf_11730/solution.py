"""
QUESTION:
Write a function named `predict_stock_market` that takes a list of tuples representing the past 10 days' stock prices, where each tuple contains the opening price, closing price, highest price, and lowest price of the day. The function should return a string indicating whether the stock market will increase, decrease, or remain stable in the next 3 days based on the given algorithm.

The function should calculate the average closing price for the past 10 days, the past 5 days, and the past 3 days, and then use the differences between these averages to make the prediction. If both differences are positive, the function should return 'increase'. If both differences are negative, the function should return 'decrease'. If one difference is positive and the other is negative, the function should return 'stable'.
"""

def predict_stock_market(stock_prices):
    """
    Predicts the stock market movement for the next 3 days based on the given past 10 days' stock prices.
    
    Args:
    stock_prices (list): A list of tuples representing the past 10 days' stock prices.
                         Each tuple contains the opening price, closing price, highest price, and lowest price of the day.
    
    Returns:
    str: A string indicating whether the stock market will increase, decrease, or remain stable in the next 3 days.
    """

    # Calculate the average closing price for the past 10 days
    avg_10_days = sum([price[1] for price in stock_prices]) / len(stock_prices)

    # Calculate the average closing price for the past 5 days
    avg_5_days = sum([price[1] for price in stock_prices[-5:]]) / 5

    # Calculate the average closing price for the past 3 days
    avg_3_days = sum([price[1] for price in stock_prices[-3:]]) / 3

    # Calculate the differences between the averages
    diff_5_10 = avg_5_days - avg_10_days
    diff_3_5 = avg_3_days - avg_5_days

    # Make the prediction based on the differences
    if diff_5_10 > 0 and diff_3_5 > 0:
        return 'increase'
    elif diff_5_10 < 0 and diff_3_5 < 0:
        return 'decrease'
    else:
        return 'stable'