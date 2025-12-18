"""
QUESTION:
Write a function `get_dates` that takes two date strings `start_date` and `end_date` as input and returns a list of all dates between `start_date` and `end_date` (inclusive) in the format "YYYY-MM-DD". The function should handle any valid date format, swap `start_date` and `end_date` if necessary, handle leap years correctly, and be efficient for large date ranges. If the date format is invalid, the function should return an empty list.
"""

from datetime import datetime, timedelta

def get_dates(start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return []

    if start_date > end_date:
        start_date, end_date = end_date, start_date

    num_days = (end_date - start_date).days
    dates = [start_date.strftime("%Y-%m-%d")]

    for i in range(1, num_days + 1):
        date = start_date + timedelta(days=i)
        dates.append(date.strftime("%Y-%m-%d"))

    return dates