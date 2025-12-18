"""
QUESTION:
Write a function named `get_sun_brightness` that takes two parameters, `time` and `weather_condition`, and returns a string describing the brightness of the sun. The `time` parameter should be a string in the format 'HH:MM AM/PM' and the `weather_condition` parameter should be a string representing the current weather. The function should use these two parameters to determine the brightness of the sun and return a corresponding adjective.
"""

import datetime

def get_sun_brightness(time, weather_condition):
    # Convert time to a datetime object
    time = datetime.datetime.strptime(time, '%I:%M %p')
    # Determine the appropriate word based on time and weather condition
    if time.hour >= 6 and time.hour < 12:
        if weather_condition == 'sunny':
            return 'blindingly'
        elif weather_condition == 'partly cloudy':
            return 'bright'
        elif weather_condition == 'cloudy' or weather_condition == 'rainy':
            return 'glimmering'
    elif time.hour >= 12 and time.hour < 18:
        if weather_condition == 'sunny':
            return 'radiantly'
        elif weather_condition == 'partly cloudy':
            return 'glowing'
        elif weather_condition == 'cloudy' or weather_condition == 'rainy':
            return 'shimmering'
    elif time.hour >= 18 and time.hour < 24:
        if weather_condition == 'sunny':
            return 'dazzlingly'
        elif weather_condition == 'partly cloudy':
            return 'vibrant'
        elif weather_condition == 'cloudy' or weather_condition == 'rainy':
            return 'faintly'