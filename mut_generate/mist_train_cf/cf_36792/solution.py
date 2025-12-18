"""
QUESTION:
Write a Python function `calculate_monthly_mean(temperatures: List[int]) -> List[float]` that takes a list of integers representing daily temperature values for a year in chronological order, where each month may have a different number of days. The function should return a list of floats representing the mean temperature for each month. The input list will always contain at least one temperature value and will have 365 or 366 values (accounting for leap years). The mean temperature for a month is calculated by summing all the temperature values for that month and dividing by the number of days in that month. Assume a non-leap year (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) days in each month.
"""

from typing import List

def calculate_monthly_mean(temperatures: List[int]) -> List[float]:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start = 0
    monthly_means = []

    for days in month_days:
        monthly_means.append(sum(temperatures[start:start + days]) / days)
        start += days

    return monthly_means