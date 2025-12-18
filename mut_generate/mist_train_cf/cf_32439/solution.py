"""
QUESTION:
Given a stream of integers and a window size, calculate the moving average for each window of the specified size as the stream progresses. Implement a function `calculate_moving_average` that takes two parameters: a list of integers `stream` and an integer `window_size`. The function should return a list of floating-point numbers representing the moving averages for each window. If the window size is larger than the length of the stream, the function should return an empty list.
"""

def movingAverage(stream, window_size):
    if window_size > len(stream):
        return []

    moving_averages = []
    window_sum = sum(stream[:window_size])
    moving_averages.append(window_sum / window_size)

    for i in range(window_size, len(stream)):
        window_sum = window_sum - stream[i - window_size] + stream[i]
        moving_averages.append(window_sum / window_size)

    return moving_averages