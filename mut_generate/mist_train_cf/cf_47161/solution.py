"""
QUESTION:
Create a function named `organize_dates_into_weeks` that takes a list of date strings in the format 'YYYY-MM-DD' as input. The function should return a dictionary where each key is a tuple representing the start and end dates of a week, and the corresponding value is a list of dates that fall within that week. The function should consider leap years and handle dates that fall on the boundary of two weeks.
"""

from datetime import datetime, timedelta

def get_week_start_end(date):
    start = date - timedelta(days=date.weekday())
    end = start + timedelta(days=6)
    return start, end

def organize_dates_into_weeks(dates):
    # Convert the dates into datetime objects
    date_objs = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

    # Organize the dates into weeks
    weeks = {}

    for date in date_objs:
        week_start_end = get_week_start_end(date)
        if week_start_end in weeks:
            weeks[week_start_end].append(date)
        else:
            weeks[week_start_end] = [date]

    return weeks