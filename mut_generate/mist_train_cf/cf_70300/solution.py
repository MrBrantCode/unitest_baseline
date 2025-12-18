"""
QUESTION:
Design a system that can forecast stock market trends using historical data. The system should include modules for data scrutiny, prediction, efficiency analysis, and risk management.
"""

def predict_stock_market_trend(historical_data):
    """
    Forecasts stock market trends using historical data.

    Parameters:
    historical_data (list): List of historical stock prices.

    Returns:
    float: Predicted stock market trend.
    """

    # Data scrutiny
    cleaned_data = [price for price in historical_data if price > 0]
    
    # Prediction engine
    predicted_trend = sum(cleaned_data) / len(cleaned_data)
    
    return predicted_trend