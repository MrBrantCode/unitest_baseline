"""
QUESTION:
Write a function called `predict_funding_rate` that takes in a list of historical funding rates and returns a predicted funding rate for the next time period. The function should be able to handle different lengths of historical data. 

The input is a list of floating point numbers representing the historical funding rates. The function should return a single floating point number representing the predicted funding rate for the next time period.
"""

def predict_funding_rate(historical_rates):
    """
    Predicts the funding rate for the next time period based on historical data.
    
    Parameters:
    historical_rates (list): A list of historical funding rates.
    
    Returns:
    float: The predicted funding rate for the next time period.
    """
    
    # Calculate the average of the historical rates
    avg_rate = sum(historical_rates) / len(historical_rates)
    
    # Simple moving average prediction: predict the next rate to be the same as the average
    return avg_rate