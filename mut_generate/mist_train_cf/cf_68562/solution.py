"""
QUESTION:
Create a function called `calculate_wind_chill(speed, temperature)` that calculates the wind chill index given the wind speed in kilometers per hour and the temperature in Celsius. The function should return the wind chill index rounded to the nearest whole number. 

The function must handle exceptional scenarios where the temperature exceeds 10 degrees Celsius or the wind speed falls below 4.8 km/h, and extreme scenarios where the wind speed exceeds 120 km/h or the temperature falls below -40 degrees Celsius. 

For exceptional scenarios, the function should return the error message "Error: The wind chill formula's reliability is compromised. Temperature must not exceed 10 degrees Celsius and wind speed must not be less than 4.8 km/h for reliable results." 

For extreme scenarios, the function should return the error message "Error: The wind chill formula's reliability is compromised under extreme conditions. Temperature must not be less than -40 degrees Celsius and wind speed must not exceed 120 km/h for reliable results." 

The function should prioritize checking for exceptional scenarios over extreme scenarios.
"""

def calculate_wind_chill(speed, temperature):
    if (temperature > 10) or (speed < 4.8):
        return "Error: The wind chill formula's reliability is compromised. Temperature must not exceed 10 degrees Celsius and wind speed must not be less than 4.8 km/h for reliable results."
    
    elif (temperature < -40) or (speed > 120):
        return "Error: The wind chill formula's reliability is compromised under extreme conditions. Temperature must not be less than -40 degrees Celsius and wind speed must not exceed 120 km/h for reliable results."
    
    else:
        wind_chill = 13.12 + 0.6215 * temperature - 11.37 * speed**0.16 + 0.3965 * temperature * speed**0.16
        return round(wind_chill)