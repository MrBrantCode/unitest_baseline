"""
QUESTION:
Create a function `get_sun_brightness(time, weather_condition)` that generates the perfect word to complete the sentence "The sun was _____ bright" for a given moment based on the provided time and weather condition. The time should be input as a string in 12-hour format ('%I:%M %p'), and the weather condition should be one of the following: 'sunny', 'partly cloudy', 'cloudy', or 'rainy'. The function should return the word that best describes the brightness of the sun.
"""

import datetime

def entrance(time, weather_condition):
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