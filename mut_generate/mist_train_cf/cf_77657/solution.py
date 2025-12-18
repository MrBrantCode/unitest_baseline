"""
QUESTION:
Create a function named `count_weekdays_in_month` that calculates the total number of weekdays (Monday to Friday) in a specific month and year. The function should take three parameters: `year`, `month`, and `holidays`, where `holidays` is a list of dates in the format "YYYY-MM-DD". The function should subtract the public holidays that fall on weekdays from the total weekday count and return the result.
"""

import calendar
import datetime

def count_weekdays_in_month(year, month, holidays):
    # Get last day of month
    last_day = calendar.monthrange(year, month)[1]
    # Define a list for weekdays (Mon-Fri)
    weekdays = [0, 1, 2, 3, 4]
    # Calculate the number of weekdays in month
    num_weekdays = len([1 for day in range(1, last_day + 1)
                            if calendar.weekday(year, month, day) in weekdays])
    # Subtract holidays falling on weekdays
    for holiday in holidays:
        holiday_date = datetime.datetime.strptime(holiday, "%Y-%m-%d").date()
        if holiday_date.year == year and holiday_date.month == month and holiday_date.weekday() in weekdays:
            num_weekdays -= 1
    return num_weekdays