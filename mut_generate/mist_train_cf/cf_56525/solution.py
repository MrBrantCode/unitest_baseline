"""
QUESTION:
Design a function called `time_converter` that takes an integer number of minutes as input and returns a string representing the equivalent duration in years, days, hours, and minutes. The function should consider leap years, which occur every 4 years, and account for the extra day in a leap year. The function should not consider daylight saving time variations and should only handle non-negative inputs.
"""

def time_converter(minutes):
    leap_year_minutes = 366 * 24 * 60
    common_year_minutes = 365 * 24 * 60
    day_minutes = 24 * 60
    hour_minutes = 60
   
    # calculate leap years and common years
    leap_years = 0
    common_years = 0
    while minutes >= common_year_minutes:
        minutes -= common_year_minutes
        common_years += 1
        if minutes >= leap_year_minutes:
            minutes += common_year_minutes  # undo last subtraction
            minutes -= leap_year_minutes  # subtract a leap year instead
            leap_years += 1
            common_years -= 1

    # calculate days
    days = minutes // day_minutes
    minutes %= day_minutes
    
    # calculate hours
    hours = minutes // hour_minutes
    minutes %= hour_minutes
    
    return f"{leap_years + common_years} years ({leap_years} leap years and {common_years} common years), {days} days, {hours} hours, {minutes} minutes"