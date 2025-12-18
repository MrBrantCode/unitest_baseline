"""
QUESTION:
Create a function `classify_and_validate_dates` that takes an array of ISO 8601 formatted date strings as input and returns two lists: a list of valid dates categorized into sequentially ordered seven-day time periods and a list of invalid ISO 8601 date strings. The function should handle leap years and identify any date strings in the array that do not conform to the ISO 8601 standard.
"""

from datetime import datetime, timedelta

def classify_and_validate_dates(dates_array):
    dates = []
    invalid_dates = []
    weeks = []
    
    for date in dates_array:
        try:
            dates.append(datetime.strptime(date, '%Y-%m-%d'))
        except ValueError:
            invalid_dates.append(date)
            
    dates.sort()
    
    while dates:
        start = dates.pop(0)
        week = [start]
        while dates and (dates[0] - start).days < 7:
            week.append(dates.pop(0))
        weeks.append(week)
    
    return weeks, invalid_dates