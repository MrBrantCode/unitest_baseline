"""
QUESTION:
Write a function named `pascal_to_bar` that takes a list of pressure measurements in Pascals as input, converts them to Bars, removes erroneous readings and outliers, and returns the maximum, minimum, and mean pressure values in Bars. The function should handle multiple readings, real-time data, and errors such as negative values and non-numeric data.
"""

import numpy as np
import statistics as stats

def remove_outliers(data):
    quartile_1, quartile_3 = np.percentile(data, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return [y for y in data if lower_bound < y < upper_bound]

def pascal_to_bar(pressure_pascal_measurements):
    clean_data = []
    for measurement in pressure_pascal_measurements:
        try:
            if measurement > 0:
                clean_data.append(measurement * 0.00001)
        except TypeError:
            return "Error: Non-numeric data detected!"
           
    if not clean_data:
        return "Error: No valid data!"
    else:    
        clean_data = remove_outliers(clean_data)
        try:
            max_pressure = max(clean_data)
            min_pressure = min(clean_data)
            mean_pressure = stats.mean(clean_data)
            return max_pressure, min_pressure, mean_pressure
        except TypeError:
            return "Error: Cannot compute statistics on non-numeric data."