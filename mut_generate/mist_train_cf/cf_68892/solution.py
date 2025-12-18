"""
QUESTION:
Construct a function called `wind_chill_index` that calculates the wind chill index given the wind speed in kilometers per hour and the temperature in Celsius. The function should return the wind chill index rounded to the nearest integer, but with the following restrictions:

- If the temperature is above 10 degrees Celsius or the wind speed is below 4.8 km/h, return "The wind chill index is not accurate under these conditions."
- If the temperature is below -40 degrees Celsius or the wind speed is above 120 km/h, return "The wind chill index is not reliable under these severe conditions."
"""

def wind_chill_index(wind_speed, temperature):
    if wind_speed < 4.8 or temperature > 10:
        return "The wind chill index is not accurate under these conditions."
    elif wind_speed > 120 or temperature < -40:
        return "The wind chill index is not reliable under these severe conditions."
    else:
        wct_index = 13.12 + 0.6215*temperature -  11.37*(wind_speed**0.16) + 0.3965*temperature*(wind_speed**0.16) 
        return round(wct_index)