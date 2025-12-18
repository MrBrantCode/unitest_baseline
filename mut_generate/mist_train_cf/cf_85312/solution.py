"""
QUESTION:
Write a function called `time_convert` that takes an integer representing a quantity of minutes as input and returns the equivalent years, days, hours, and minutes. Assume a year has 525,600 minutes and a day has 1,440 minutes.
"""

def time_convert(minutes):
    minutes_in_a_year = 525600
    minutes_in_a_day = 1440
    minutes_in_an_hour = 60

    years = minutes // minutes_in_a_year
    minutes -= years * minutes_in_a_year

    days = minutes // minutes_in_a_day
    minutes -= days * minutes_in_a_day

    hours = minutes // minutes_in_an_hour
    minutes -= hours * minutes_in_an_hour

    return years, days, hours, minutes