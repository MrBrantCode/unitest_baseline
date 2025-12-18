"""
QUESTION:
Write a function `convert_days(days)` to convert a given number of days into years, months, weeks, and days. The function should assume each month has 30 days and each year has 365 days. It should return the number of years, months, weeks, and remaining days.
"""

def convert_days(days):
    years = days // 365
    months = (days % 365) // 30
    weeks = ((days % 365) % 30) // 7
    remaining_days = ((days % 365) % 30) % 7

    return years, months, weeks, remaining_days