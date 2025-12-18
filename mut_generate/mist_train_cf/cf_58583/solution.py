"""
QUESTION:
Design an algorithm to categorize a series of dates into consecutive weekly intervals, handling non-chronological order and inconsistent or erroneous dates. Create a function `categorize_dates(dates)` that takes a list of date strings in "YYYY-MM-DD" format as input and returns a list of lists, where each sublist contains dates within a consecutive weekly interval.
"""

from datetime import datetime, timedelta

def categorize_dates(dates): 
    try:
        sorted_dates = sorted(dates, key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
    except ValueError:
        return "You have provided an invalid date. Ensure dates are in 'YYYY-MM-DD' format and valid."
    
    weekly_intervals = []
    week = []

    start_date = datetime.strptime(sorted_dates[0], "%Y-%m-%d")
    for date in sorted_dates:
        current_date = datetime.strptime(date, "%Y-%m-%d")
        if (current_date - start_date).days < 7:
            week.append(date)
        else:
            weekly_intervals.append(week)
            week = [date]
            start_date = current_date 

    if week:
        weekly_intervals.append(week)

    return weekly_intervals