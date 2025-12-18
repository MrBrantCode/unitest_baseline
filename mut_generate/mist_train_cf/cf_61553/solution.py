"""
QUESTION:
Compute the wind chill index for given temperature and wind speed values. 

Develop a function named `compute_wind_chill` that takes in two lists of numbers, `temps` and `wind_speeds`, representing temperatures in Celsius and wind speeds in kilometers per hour respectively. The function should calculate the wind chill index for each pair of temperature and wind speed values, rounding to the nearest whole number. 

However, the wind chill formula's reliability is compromised under certain circumstances: 
- Temperature exceeds 10 degrees Celsius
- Wind speed falls below 4.8 km/h
- Wind speed exceeds 120 km/h

In such cases, the function should return an error message instead of the wind chill index. The function should return a list of results, with each result being either the computed wind chill index or an error message.
"""

import numpy as np

def compute_wind_chill(temps, wind_speeds):
    results = []
    for temp, wind_speed in zip(temps, wind_speeds):
        if temp > 10:
            results.append("Error: Temperature over 10 degrees Celsius")
        elif wind_speed < 4.8:
            results.append("Error: Windspeed below 4.8 km/h")
        elif wind_speed > 120:
            results.append("Error: Windspeed over 120 km/h")
        else:
            wind_chill_index = 13.12 + 0.6215*temp - 11.37*wind_speed**0.16 + 0.3965*temp*wind_speed**0.16
            rounded_index = int(np.round(wind_chill_index))
            results.append(rounded_index)
    return results