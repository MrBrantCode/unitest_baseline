"""
QUESTION:
Write a Python function `is_stationary` that determines whether a given time series is stationary or not based on its statistical properties. The function should consider the mean, variance, and autocorrelation of the series, and return `True` if these properties are constant over time, indicating a stationary series, and `False` otherwise.
"""

def is_stationary(time_series):
    """
    Determines whether a given time series is stationary or not based on its statistical properties.

    Args:
    time_series (list): A list of numbers representing the time series.

    Returns:
    bool: True if the time series is stationary, False otherwise.
    """
    
    # Calculate the mean of the time series
    mean = sum(time_series) / len(time_series)
    
    # Calculate the variance of the time series
    variance = sum((x - mean) ** 2 for x in time_series) / len(time_series)
    
    # Calculate the autocorrelation of the time series
    autocorrelation = sum((time_series[i] - mean) * (time_series[i-1] - mean) for i in range(1, len(time_series))) / (len(time_series) - 1)
    
    # Check if the mean, variance, and autocorrelation are constant over time
    # For simplicity, we assume that if the absolute difference between the current value and the previous value is less than 0.01, they are considered constant
    for i in range(1, len(time_series)):
        current_mean = sum(time_series[:i+1]) / (i+1)
        current_variance = sum((x - current_mean) ** 2 for x in time_series[:i+1]) / (i+1)
        current_autocorrelation = sum((time_series[j] - current_mean) * (time_series[j-1] - current_mean) for j in range(1, i+1)) / i
        
        if abs(current_mean - mean) > 0.01 or abs(current_variance - variance) > 0.01 or abs(current_autocorrelation - autocorrelation) > 0.01:
            return False
    
    return True