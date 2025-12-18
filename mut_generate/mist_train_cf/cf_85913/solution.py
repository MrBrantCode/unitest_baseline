"""
QUESTION:
Develop a function `compute_wind_chill(v, t)` that calculates the wind chill index given the wind speed in kilometers per hour (`v`) and the ambient temperature in degrees Celsius (`t`). The result should be rounded to the nearest whole number. The function should raise an exception if the temperature exceeds 10 degrees Celsius or the wind speed is below 4.8 km/h, as the wind chill equation becomes unreliable under these circumstances.
"""

import math

def compute_wind_chill(v, t):
    if t > 10 or v < 4.8:
        raise Exception('The wind chill equation becomes unreliable under these circumstances.')
    
    wci = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
    return round(wci)