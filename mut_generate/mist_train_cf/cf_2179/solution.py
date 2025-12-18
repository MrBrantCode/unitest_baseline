"""
QUESTION:
Write a function `get_weekday_count(start_date, end_date)` that takes two dates in the format DD MMM YYYY as input and returns the number of weekdays (excluding weekends and public holidays) between these two dates. The function should handle leap years correctly and account for any changes in the number of weekdays in a week due to public holidays or observances. Public holidays should be defined as fixed dates that are observed every year.
"""

import datetime

def is_weekday(date):
    return date.weekday() < 5

def is_public_holiday(date):
    public_holidays = {
        datetime.date(2020, 5, 25): "Memorial Day",
        datetime.date(2020, 6, 4): "Eid al-Fitr"
        # Add more public holidays here
    }
    return date in public_holidays

def get_weekday_count(start_date, end_date):
    try:
        start_date = datetime.datetime.strptime(start_date, "%d %b %Y").date()
        end_date = datetime.datetime.strptime(end_date, "%d %b %Y").date()
    except ValueError:
        return "Invalid date format"
    
    if start_date > end_date:
        return "Start date should be before end date"

    weekday_count = 0
    current_date = start_date

    while current_date <= end_date:
        if is_weekday(current_date) and not is_public_holiday(current_date):
            weekday_count += 1
        current_date += datetime.timedelta(days=1)

    return weekday_count