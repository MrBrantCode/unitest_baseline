"""
QUESTION:
Write a function called `wind_chill_index` that calculates the wind chill index given the temperature in Celsius and the wind speed in kilometers per hour. The wind chill index should be rounded to the nearest whole number. The function should return an error message if the temperature exceeds 10 degrees Celsius or the wind speed falls below 4.8 km/h, as the wind chill formula is unreliable under these conditions.
"""

def wind_chill_index(temperature, wind_speed):
    if temperature > 10:
        return "Error: Temperature exceeds 10 degrees Celsius. Wind chill formula's reliability is compromised."
    elif wind_speed < 4.8:
        return "Error: Wind speed falls below 4.8 km/h. Wind chill formula's reliability is compromised."
    else:
        wind_speed_m_s = wind_speed / 3.6   #Converting km/h to m/s
        WCI = 13.12 + 0.6215*temperature -  11.37*(wind_speed_m_s**0.16) + 0.3965*temperature*(wind_speed_m_s**0.16)
        return round(WCI)