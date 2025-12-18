"""
QUESTION:
Write a function `convert_to_gregorian` that takes a Julian date string in the format "YYYYDDD" (where DDD is the day of the year from 1 to 366) as input and returns the equivalent Gregorian date string in the format "DD-MM-YYYY".
"""

from datetime import datetime, timedelta

def convert_to_gregorian(julian_date):
    year = int(julian_date[:4])
    day = int(julian_date[4:])

    gregorian_date = datetime(year, 1, 1) + timedelta(day - 1)

    return gregorian_date.strftime("%d-%m-%Y")