"""
QUESTION:
Create a function `gen_ah_lut(t_range)` that takes a temperature range `t_range` and returns a list of Absolute Humidity (AH) values at 100% Relative Humidity (RH) corresponding to the temperatures in the range. The AH values should be calculated using the formula `AH = k * rh * exp(m * t)`, where `k` and `m` are constants, `t` is the temperature, and `rh` is the relative humidity (fixed at 100%). The function should scale the AH values linearly from 0 to 100.
"""

import math

def gen_ah_lut(t_range):
    """ Generate the AH Look Up Table at 100%RH (0..100 scales linearly) """
    k = 0.622
    m = 17.62
    lut = []
    for t in t_range:
        ah_100_rh = k * 100 * math.exp(m * (t - 273.15) / (237.3 + (t - 273.15))) # Convert to Celsius to Kelvin 
        lut.append(ah_100_rh)
    return lut