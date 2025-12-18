"""
QUESTION:
Create a function named `convert_seconds` that takes an integer number of seconds as input and returns a tuple containing the equivalent number of years, months, weeks, days, hours, minutes, and seconds. Assume a year has 365 days, a month has 30 days, and a week has 7 days.
"""

def convert_seconds(seconds):
    years = seconds // (365 * 24 * 60 * 60)
    seconds %= (365 * 24 * 60 * 60)
    
    months = seconds // (30 * 24 * 60 * 60)
    seconds %= (30 * 24 * 60 * 60)
    
    weeks = seconds // (7 * 24 * 60 * 60)
    seconds %= (7 * 24 * 60 * 60)
    
    days = seconds // (24 * 60 * 60)
    seconds %= (24 * 60 * 60)
    
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    
    minutes = seconds // 60
    seconds %= 60
    
    return years, months, weeks, days, hours, minutes, seconds