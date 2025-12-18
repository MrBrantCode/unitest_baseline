"""
QUESTION:
Create a function called `celsius_to_fahrenheit` that takes four parameters: temperature in Celsius, altitude in meters, time of day (either 'day' or 'night'), and season (either 'summer' or 'winter'). The function should first adjust the temperature based on the altitude by subtracting 1 degree Celsius for every 100 meters above 1000 meters. Then it should adjust the temperature based on the time of day and season. Finally, it should convert the temperature from Celsius to Fahrenheit using the formula F = (C * 1.8) + 32 and return the result.
"""

def celsius_to_fahrenheit(celsius, altitude, time_of_day, season):
    if altitude > 1000:
        celsius -= (altitude - 1000) // 100
    if time_of_day == 'day' and season == 'summer':
        celsius += 5
    elif time_of_day == 'day' and season == 'winter':
        celsius += 2
    elif time_of_day == 'night' and season == 'summer':
        celsius += 2
    elif time_of_day == 'night' and season == 'winter':
        celsius -= 5
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit