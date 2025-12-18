"""
QUESTION:
Convert the given number of seconds to years, months, weeks, days, hours, minutes, and seconds using the function `convert_seconds(seconds)`. The input can be up to 10^18 seconds. Consider leap years when calculating days and months. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def convert_seconds(seconds):
    seconds_in_year = 365 * 24 * 60 * 60
    seconds_in_month = 30 * 24 * 60 * 60
    seconds_in_week = 7 * 24 * 60 * 60
    seconds_in_day = 24 * 60 * 60
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    years = seconds // seconds_in_year
    seconds %= seconds_in_year
    
    months = seconds // seconds_in_month
    seconds %= seconds_in_month
    
    weeks = seconds // seconds_in_week
    seconds %= seconds_in_week
    
    days = seconds // seconds_in_day
    seconds %= seconds_in_day
    
    hours = seconds // seconds_in_hour
    seconds %= seconds_in_hour
    
    minutes = seconds // seconds_in_minute
    seconds %= seconds_in_minute
    
    return years, months, weeks, days, hours, minutes, seconds