"""
QUESTION:
Create a function called `convert_seconds(seconds)` that takes a number of seconds as input and returns a string representing the equivalent time in years, months, weeks, days, hours, minutes, and seconds. The function should account for leap years and different month lengths, but does not need to handle time zones or daylight saving time changes.
"""

def convert_seconds(seconds):
    year_seconds = 365.25 * 24 * 60 * 60  
    month_seconds = (365.25 * 24 * 60 * 60) / 12  
    week_seconds = 7 * 24 * 60 * 60  
    day_seconds = 24 * 60 * 60  
    hour_seconds = 60 * 60  
    minute_seconds = 60  

    years = seconds // year_seconds
    seconds %= year_seconds

    months = seconds // month_seconds
    seconds %= month_seconds

    weeks = seconds // week_seconds
    seconds %= week_seconds

    days = seconds // day_seconds
    seconds %= day_seconds

    hours = seconds // hour_seconds
    seconds %= hour_seconds

    minutes = seconds // minute_seconds
    seconds %= minute_seconds

    return f"{int(years)} years, {int(months)} months, {int(weeks)} weeks, {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"