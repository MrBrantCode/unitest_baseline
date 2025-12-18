"""
QUESTION:
Create a function called `calculate_avg_and_std` that takes a list of strings in the format "measurement=value" as input, where "value" is a floating-point number, and returns a tuple of two floating-point numbers representing the average and standard deviation of the measurements. The function should return 0 as the standard deviation if the input list contains only one measurement.
"""

import re
import statistics

def calculate_avg_and_std(measurements):
    values = [float(re.search(r'measurement=([\d.]+)', measurement).group(1)) for measurement in measurements if re.search(r'measurement=([\d.]+)', measurement)]
    avg = sum(values) / len(values)
    std_dev = statistics.stdev(values) if len(values) > 1 else 0
    return avg, std_dev