"""
QUESTION:
Implement a function `rma` that calculates the rolling mean of a list of numbers. The function takes a list of numbers `data` and a window size `window_size` as input, and returns a new list containing the rolling mean values. The rolling mean is calculated by averaging the numbers within a sliding window of size `window_size`. The function should return a list of rolling mean values, where each value is the average of the corresponding window in the input data. The function should return an empty list if the window size is larger than the input data.
"""

from typing import List

def rma(data: List[float], window_size: int) -> List[float]:
    if window_size > len(data):
        return []

    rolling_means = []
    window_sum = sum(data[:window_size])

    for i in range(len(data) - window_size + 1):
        if i == 0:
            rolling_means.append(window_sum / window_size)
        else:
            window_sum = window_sum - data[i - 1] + data[i + window_size - 1]
            rolling_means.append(window_sum / window_size)

    return rolling_means