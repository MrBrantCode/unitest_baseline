"""
QUESTION:
Create a function named `convert(minutes)` that takes an integer number of minutes as input and returns the equivalent time broken down into years, days, hours, and minutes. Assume a year has 365 days.
"""

def convert(minutes):
    # Constants representing number of minutes per unit
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_YEAR = 365

    # Calculate the number of years
    years = minutes // (MINUTES_PER_HOUR * HOURS_PER_DAY * DAYS_PER_YEAR)
    minutes %= MINUTES_PER_HOUR * HOURS_PER_DAY * DAYS_PER_YEAR

    # Calculate the number of days
    days = minutes // (MINUTES_PER_HOUR * HOURS_PER_DAY)
    minutes %= MINUTES_PER_HOUR * HOURS_PER_DAY

    # Calculate the number of hours
    hours = minutes // MINUTES_PER_HOUR
    minutes %= MINUTES_PER_HOUR

    return years, days, hours, minutes