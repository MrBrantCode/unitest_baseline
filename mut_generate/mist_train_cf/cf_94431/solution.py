"""
QUESTION:
Create a function `count_weekdays` that calculates the number of weekdays (Monday to Friday) between two given dates in the format 'YYYY-MM-DD'. The function should consider leap years, handle invalid date inputs, and optimize for large date ranges.
"""

import datetime

def count_weekdays(date1, date2):
    try:
        start_date = datetime.datetime.strptime(date1, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(date2, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return None
    
    if start_date > end_date:
        print("Start date cannot be later than end date.")
        return None
    
    weekdays = 0
    current_date = start_date
    
    while current_date <= end_date:
        if current_date.weekday() < 5:  # Monday to Friday
            weekdays += 1
        current_date += datetime.timedelta(days=1)
    
    return weekdays