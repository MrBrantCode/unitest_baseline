"""
QUESTION:
Create a function `calculate_days_between_dates(start_date, end_date)` that takes two date strings in the format "YYYY-MM-DD" as input and returns the number of days between the two dates, inclusive of the start date and end date.
"""

from datetime import datetime

def calculate_days_between_dates(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return (end - start).days + 1