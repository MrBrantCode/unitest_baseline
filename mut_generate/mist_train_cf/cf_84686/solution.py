"""
QUESTION:
Write a function named `predict_prices` that takes a list of the last five trading days' stock prices and returns a list of predicted prices for the next three trading days. The function should use a simple predictive model based on the average of the input prices. The output should be a list of three floats, each rounded to two decimal places, representing the predicted prices for the next three trading days.
"""

def predict_prices(prices):
    last_five_days_average_price = sum(prices) / len(prices)
    return [round(last_five_days_average_price, 2)] * 3