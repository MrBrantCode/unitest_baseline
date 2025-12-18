"""
QUESTION:
Create a function called `celsius_to_fahrenheit` that takes four inputs: temperature in Celsius, altitude in meters, time of day (either 'day' or 'night'), and season (either 'summer' or 'winter'). The function should consider the altitude, time of day, and season when converting the temperature from Celsius to Fahrenheit. If the altitude is above 1000 meters, subtract 1 degree Celsius for every 100 meters above sea level. Adjust the temperature based on the time of day and season according to the following rules: add 5 degrees Fahrenheit for daytime in summer, add 2 degrees Fahrenheit for daytime in winter, add 2 degrees Fahrenheit for nighttime in summer, and subtract 5 degrees Fahrenheit for nighttime in winter. Finally, convert the temperature from Celsius to Fahrenheit using the formula F = (C * 1.8) + 32.
"""

import math

def entrance(celsius, altitude, time_of_day, season):
    if altitude > 1000:
        celsius -= (altitude - 1000) // 100
    if time_of_day == 'day' and season == 'summer':
        celsius += 5 / 1.8
    elif time_of_day == 'day' and season == 'winter':
        celsius += 2 / 1.8
    elif time_of_day == 'night' and season == 'summer':
        celsius += 2 / 1.8
    elif time_of_day == 'night' and season == 'winter':
        celsius -= 5 / 1.8
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit