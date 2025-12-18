"""
QUESTION:
Write a function named `day_of_the_week` that takes a string date in the format "YYYY/MM/DD" as input and returns the corresponding day of the week as a string. Assume the input date is always valid and in the specified format.
"""

from datetime import datetime

def day_of_the_week(date: str) -> str:
    parsed_date = datetime.strptime(date, "%Y/%m/%d")
    day_of_week = parsed_date.strftime("%A")
    return day_of_week