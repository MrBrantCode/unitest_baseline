"""
QUESTION:
Write a function named `days_until_start_of_week` that takes a current date (`current_date`) and a list of dates retrieved from a database (`days_from_database`) as input, and returns the number of days between the `current_date` and the start of the current week. Assume the week starts on Sunday. Note that the `days_from_database` is not used in the function and is only included as part of the function signature. The function should return an integer value.
"""

from datetime import datetime, timedelta
from typing import List

def days_until_start_of_week(current_date: datetime, days_from_database: List[datetime]) -> int:
    start_of_week = current_date - timedelta(days=current_date.weekday())
    return (current_date - start_of_week).days