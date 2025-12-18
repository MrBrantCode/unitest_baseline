"""
QUESTION:
Implement a function `calculate_moving_average` that calculates the moving average of a list of numbers. The function should take in four parameters: `data`, a list of numerical data points; `window_size`, an integer representing the size of the window; `skipna`, a boolean indicating whether to exclude NaN values; and `iterate`, a boolean indicating whether to iterate over the data list. The function should return a list of moving average values based on the input data and window size, handling the skipna and iterate parameters accordingly.
"""

import math
import itertools

def calculate_moving_average(data, window_size, skipna=False, iterate=True):
    moving_averages = []
    if iterate:
        for i in range(len(data) - window_size + 1):
            subset = data[i:i + window_size]
            if skipna:
                subset = [x for x in subset if not isinstance(x, float) or not math.isnan(x)]
            average = sum(subset) / len(subset) if subset else None
            moving_averages.append(average)
    else:
        if skipna:
            data = [x for x in data if not isinstance(x, float) or not math.isnan(x)]
        cumsum = [0] + list(itertools.accumulate(data))
        for i in range(window_size, len(data) + 1):
            subset_sum = cumsum[i] - cumsum[i - window_size]
            average = subset_sum / window_size
            moving_averages.append(average)
    return moving_averages