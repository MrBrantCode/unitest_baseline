"""
QUESTION:
Create a function `convert_seconds(seconds)` that converts a given number of seconds into a more readable format of years, months, weeks, days, hours, minutes, and seconds. The function should account for leap years and different month lengths. It should return a string representing the time duration in the format "X years, Y months, Z weeks, A days, B hours, C minutes, D seconds".
"""

def convert_seconds(seconds):
    year_seconds = 365.25 * 24 * 60 * 60  # Average seconds in a year accounting for leap years
    month_seconds = (365.25 * 24 * 60 * 60) / 12  # Average seconds in a month accounting for leap years
    week_seconds = 7 * 24 * 60 * 60  # Seconds in a week
    day_seconds = 24 * 60 * 60  # Seconds in a day
    hour_seconds = 60 * 60  # Seconds in an hour
    minute_seconds = 60  # Seconds in a minute

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