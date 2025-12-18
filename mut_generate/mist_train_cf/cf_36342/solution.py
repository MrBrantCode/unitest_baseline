"""
QUESTION:
Write a function `day_of_week(months, d)` that takes a list of integers `months` representing the number of days in each month of a non-leap year and an integer `d` representing a day of the year (1-indexed), and returns the day of the week corresponding to the given day of the year. Assume that January 1st is a Sunday.
"""

from typing import List

def day_of_week(months: List[int], d: int) -> str:
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    sumOfMonths = sum(months[:d//31])
    result = sumOfMonths + d - 1
    return days[result % 7]