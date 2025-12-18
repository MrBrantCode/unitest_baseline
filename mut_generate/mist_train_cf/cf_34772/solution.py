"""
QUESTION:
Implement a `RangeTimePlot` class with `add_data_point(timestamp, value)` and `generate_plot(start_time, end_time)` methods. The `add_data_point` method should add a data point with a given timestamp and value. The `generate_plot` method should print a time plot of data points within a specified time range (inclusive of start and end times) with timestamps on the x-axis and corresponding values on the y-axis.
"""

def range_time_plot(data_points, start_time, end_time):
    time_plot = [f"{timestamp} | {value}" for timestamp, value in data_points if start_time <= timestamp <= end_time]
    return "Time Plot:\n" + "\n".join(time_plot)