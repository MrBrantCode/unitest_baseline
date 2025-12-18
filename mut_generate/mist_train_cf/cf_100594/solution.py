"""
QUESTION:
Create a function `get_sun_brightness(time, weather_condition)` that takes two parameters: `time` (a string representing the time of day in 12-hour format, e.g., '2:00 PM') and `weather_condition` (a string representing the current weather condition, e.g., 'sunny', 'partly cloudy', 'cloudy', or 'rainy'). The function should return an adjective (string) to complete the sentence "The sun was _____ bright" based on the given time and weather condition.
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