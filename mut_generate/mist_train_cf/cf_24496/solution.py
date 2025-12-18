"""
QUESTION:
Design a function `detect_anomaly` that takes a pandas DataFrame as input, containing two columns 'temperature' and 'pressure'. The function should detect anomalies in the data using a threshold of 3 standard deviations from the mean, and mark them in a new column 'anomaly' with a value of 1, while normal data points are marked with 0. The function should return the updated DataFrame.
"""

import numpy as np
import pandas as pd

def detect_anomaly(data):
    mean_1 = np.mean(data['temperature'])
    mean_2 = np.mean(data['pressure'])
    sd_1 = np.std(data['temperature'])
    cutoff = sd_1 * 3

    lower_limit_temperature = mean_1 - cutoff
    upper_limit_temperature = mean_1 + cutoff
    lower_limit_pressure = mean_2 - (np.std(data['pressure']) * 3)
    upper_limit_pressure = mean_2 + (np.std(data['pressure']) * 3)

    data['anomaly'] = 0
    data.loc[(data['temperature'] < lower_limit_temperature) | (data['temperature'] > upper_limit_temperature) | 
             (data['pressure'] < lower_limit_pressure) | (data['pressure'] > upper_limit_pressure), 'anomaly'] = 1
    return data