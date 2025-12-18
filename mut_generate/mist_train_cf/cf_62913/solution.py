"""
QUESTION:
Implement a function called `impute_additive_outliers` to replace additive outliers in a given time series with the average of the previous and next observation.
"""

def impute_additive_outliers(time_series):
    """
    Replace additive outliers in a given time series with the average of the previous and next observation.

    Args:
        time_series (list): The input time series data.

    Returns:
        list: The time series with additive outliers replaced.
    """
    result = [time_series[0]]  # start with the first element
    for i in range(1, len(time_series) - 1):
        if abs(time_series[i] - time_series[i-1]) > 2 * abs(time_series[i+1] - time_series[i-1]):  # assume additive outlier if difference with previous is more than twice the difference with next
            result.append((time_series[i-1] + time_series[i+1]) / 2)  # replace with average of previous and next
        else:
            result.append(time_series[i])
    result.append(time_series[-1])  # append the last element
    return result