"""
QUESTION:
Write a function called `smooth_rolling_sum` that takes a list of numbers representing time series data and an integer `window_size` representing the size of the rolling window. The function should return a list of smoothed rolling sums, adjusting for significant changes due to old data dropping out of the window.
"""

def smooth_rolling_sum(data, window_size):
    """
    Calculate the smoothed rolling sum of a list of numbers, adjusting for significant changes due to old data dropping out of the window.

    Args:
        data (list): A list of numbers representing time series data.
        window_size (int): The size of the rolling window.

    Returns:
        list: A list of smoothed rolling sums.
    """
    if not data or window_size <= 0:
        return []

    # Initialize the result list with zeros
    result = [0] * len(data)

    # Calculate the cumulative sum of the data
    cumulative_sum = [0] * (len(data) + 1)
    for i in range(len(data)):
        cumulative_sum[i + 1] = cumulative_sum[i] + data[i]

    # Calculate the smoothed rolling sum
    for i in range(len(data)):
        start = max(0, i - window_size + 1)
        result[i] = (cumulative_sum[i + 1] - cumulative_sum[start]) / (i - start + 1)

    return result