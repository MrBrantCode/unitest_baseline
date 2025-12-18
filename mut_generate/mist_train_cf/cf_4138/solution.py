"""
QUESTION:
Write a function `convert_days` that takes an integer number of days as input and returns the equivalent number of years, months, weeks, and days. The function should handle negative input, consider leap years, and accurately account for the number of days in each month.
"""

def convert_days(days):
    # Calculate the sign of the input number
    sign = -1 if days < 0 else 1
    days = abs(days)

    # Calculate the number of years
    years = days // 365
    days = days % 365

    # Calculate the number of months
    months = days // 30
    days = days % 30

    # Calculate the number of weeks
    weeks = days // 7
    days = days % 7

    # Return the converted values with the correct sign
    return sign * years, sign * months, sign * weeks, sign * days