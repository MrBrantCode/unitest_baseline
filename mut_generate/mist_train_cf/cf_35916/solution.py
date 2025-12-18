"""
QUESTION:
Implement the function `calculate_weeks(start_date: str, end_date: str) -> int` that calculates the number of weeks between a given date and a fixed start date "2021-01-04", excluding weekends. The input date should be in the format "YYYY-MM-DD". The function should return the number of weeks (rounded down to the nearest integer) between the start date and the end date, excluding weekends. Assume the input date is always after or equal to the start date and in the format "YYYY-MM-DD".
"""

from datetime import datetime, timedelta

def entance(start_date: str, end_date: str) -> int:
    start = datetime.strptime("2021-01-04", "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    days_diff = (end - start).days

    weeks = days_diff // 7  
    remaining_days = days_diff % 7  

    if remaining_days > 0:
        end_weekday = (start + timedelta(days=days_diff)).weekday()
        if end_weekday < start.weekday():
            remaining_days -= 2  
        elif end_weekday == 5:
            remaining_days -= 1 
        weeks += 1 if remaining_days > 0 else 0

    return weeks