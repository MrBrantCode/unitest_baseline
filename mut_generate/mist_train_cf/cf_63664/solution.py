"""
QUESTION:
Design a function `median_humidity` that takes three arrays `city1`, `city2`, and `city3` as input, each representing humidity levels for 7 days. Return an array of size 3 with the median humidity levels of each city and the index (0-6) of the day with the maximum median humidity across all cities. If multiple days have the same maximum humidity, return the smallest index. Handle edge cases where a single array has the same elements or some arrays are empty.
"""

import numpy as np

def median_humidity(city1, city2, city3):
    cities = [city1, city2, city3]
    median_humidity_levels = []

    if all([not city for city in cities]):
        return [], "None of the arrays have elements"

    for city in cities:
        if not city:
            median_humidity_levels.append(0)
            continue
        median_humidity_levels.append(np.median(city))

    max_median_humidity = max(median_humidity_levels)
    max_median_humidity_day = median_humidity_levels.index(max_median_humidity)
    
    return median_humidity_levels, max_median_humidity_day