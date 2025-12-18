"""
QUESTION:
Create a function `calculate_minutes_and_seconds(seconds)` that takes an integer `seconds` as input and returns a tuple `(minutes, remaining_seconds)` where `minutes` is the total number of minutes less the whole hour and `remaining_seconds` is the remaining seconds after calculating the minutes.
"""

def entrance(seconds):
    minutes = seconds // 60  
    remaining_seconds = seconds % 60  
    minutes_less_whole_hour = minutes % 60  

    return (minutes_less_whole_hour, remaining_seconds)