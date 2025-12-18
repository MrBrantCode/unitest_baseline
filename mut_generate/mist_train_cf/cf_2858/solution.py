"""
QUESTION:
Write a function named `convert_time` that takes an integer representing the hour of a day in Central Daylight Time (CDT) and returns the corresponding hour in Eastern Standard Time (EST), considering the 2-hour difference between the two time zones during the daylight saving time transition.
"""

def convert_time(cdt_time):
    est_time = cdt_time + 2
    if est_time >= 24:
        est_time -= 24
    return est_time