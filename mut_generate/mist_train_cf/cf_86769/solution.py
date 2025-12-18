"""
QUESTION:
Create a function named `convert_seconds` that takes an integer representing a number of seconds as input and returns a string representing the equivalent duration in years, months, weeks, days, hours, minutes, and seconds. Implement the function manually without using any external libraries or modules, assuming a month is 30 days and a year is 365 days.
"""

def convert_seconds(seconds):
    # Define the number of seconds in each time unit
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    week = 7 * day
    month = 30 * day
    year = 365 * day

    # Calculate the number of years, months, weeks, days, hours, minutes, and seconds
    years = seconds // year
    seconds %= year
    months = seconds // month
    seconds %= month
    weeks = seconds // week
    seconds %= week
    days = seconds // day
    seconds %= day
    hours = seconds // hour
    seconds %= hour
    minutes = seconds // minute
    seconds %= minute

    # Construct the readable format string
    result = ""
    if years > 0:
        result += f"{years} year{'s' if years > 1 else ''}, "
    if months > 0:
        result += f"{months} month{'s' if months > 1 else ''}, "
    if weeks > 0:
        result += f"{weeks} week{'s' if weeks > 1 else ''}, "
    if days > 0:
        result += f"{days} day{'s' if days > 1 else ''}, "
    if hours > 0:
        result += f"{hours} hour{'s' if hours > 1 else ''}, "
    if minutes > 0:
        result += f"{minutes} minute{'s' if minutes > 1 else ''}, "
    if seconds > 0:
        result += f"{seconds} second{'s' if seconds > 1 else ''}, "

    # Remove trailing comma and space
    result = result.rstrip(", ")

    return result