"""
QUESTION:
Construct an algorithm to predict the next 3 days' stock market movements given the stock prices from the past 5 days. The function should take a list of past stock prices as input and return a list of predicted values. The prediction should be based on the average of three consecutive days and the difference in market movement between consecutive days. The function name should be predict_stock_movements.
"""

def predict_stock_movements(data):
    # Initialize empty list to store predicted values
    predictions = []

    # Iterate over the given data
    for i in range(len(data)-2):
        # Calculate the average of the 3 consecutive days
        avg = sum(data[i:i+3])/3
        # Calculate the current and past day market movement
        curr_mov = data[i+2] - data[i+1]
        past_mov = data[i+1] - data[i]
        # Predict the next day
        prediction = avg + curr_mov + past_mov
        predictions.append(prediction)

    return predictions