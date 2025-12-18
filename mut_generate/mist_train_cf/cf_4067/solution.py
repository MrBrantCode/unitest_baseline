"""
QUESTION:
Write a function `predict_stock_movement` that takes a list of 10 tuples representing the past 10 days' stock prices and returns a list of 3 integers representing the predicted stock market movements for the next 3 days. Each tuple should contain six elements: the opening price, closing price, highest price, lowest price, the percentage change in the stock price compared to the previous day, and the trading volume for the day. The function should consider the trading volume only for the past 10 days and assume the input list is sorted in chronological order with the most recent day first. The predicted movements should be represented as 1 for a positive movement, -1 for a negative movement, and 0 for no significant movement.
"""

def predict_stock_movement(prices):
    predictions = []
    
    # Calculate the average percentage change in stock price over the past 10 days
    avg_percent_change = sum([price[4] for price in prices]) / len(prices)
    
    # Calculate the average trading volume over the past 10 days
    avg_volume = sum([price[5] for price in prices]) / len(prices)
    
    # Iterate through the past 10 days' stock prices
    for i in range(10):
        # Calculate the difference between the highest price and the lowest price for each day's stock price
        price_range = prices[i][2] - prices[i][3]
        
        # Determine the predicted movement for the current day based on the above conditions
        if prices[i][1] > prices[i][0] and prices[i][4] > avg_percent_change:
            predictions.append(1)
        elif prices[i][1] < prices[i][0] and prices[i][4] < avg_percent_change:
            predictions.append(-1)
        elif prices[i][5] > avg_volume:
            predictions.append(predictions[-1] if predictions else 0)
        else:
            predictions.append(0)
    
    # Since we've iterated over 10 days, we only need the last 3 predictions
    return predictions[-3:]