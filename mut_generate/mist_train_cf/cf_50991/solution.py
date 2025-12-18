"""
QUESTION:
Create a function named `calculate_wind_chill` that takes two parameters: ambient temperature in degrees Celsius and wind speed in kilometers per hour. The function must calculate the wind chill index using the formula 13.12 + 0.6215T - 11.37V^0.16 + 0.3965TV^0.16, where T is the temperature and V is the wind speed, and return the result rounded to the nearest integer. However, the function should return a custom error message if the temperature exceeds 10 degrees Celsius or the wind speed is less than 4.8 km/h, as the wind chill formula becomes unreliable under these conditions.
"""

def calculate_wind_chill(temp, wind_speed):
    if temp > 10:
        return "Error: Temperature is too high for the wind chill index to be reliable."
    if wind_speed < 4.8:
        return "Error: Wind speed is too low for the wind chill index to be reliable."
    wind_chill = 13.12 + 0.6215*temp - 11.37*(wind_speed**0.16) + 0.3965*temp*(wind_speed**0.16)
    return round(wind_chill)