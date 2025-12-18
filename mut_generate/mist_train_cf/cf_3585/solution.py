"""
QUESTION:
Write a function called "calculate_weekdays" that calculates the number of weekdays taken to finish a task given its start and end dates. The function should take three parameters: start_date, end_date, and holidays. The start_date and end_date should be dates, and the holidays should be a list of dates. The task must be completed within a maximum of 30 weekdays and cannot be completed on weekends or holidays. Weekdays are defined as Monday to Friday. If the start and end dates are the same, or if either date is a weekend or holiday, the task is considered to be completed in 0 weekdays. If the start date is a weekend or holiday, the task starts on the next weekday, and if the end date is a weekend or holiday, the task ends on the previous weekday. If the start date is after the end date, the task is considered to be completed in 0 weekdays. The function should return the number of weekdays taken to complete the task.
"""

import datetime

def calculate_weekdays(start_date, end_date, holidays):
    # If the start and end dates are the same, return 0
    if start_date == end_date:
        return 0

    # If the start date is after the end date, return 0
    if start_date > end_date:
        return 0

    # If the start date is a weekend or holiday, move to the next weekday
    while start_date.weekday() >= 5 or start_date in holidays:
        start_date += datetime.timedelta(days=1)

    # If the end date is a weekend or holiday, move to the previous weekday
    while end_date.weekday() >= 5 or end_date in holidays:
        end_date -= datetime.timedelta(days=1)

    # Calculate the total number of days between the start and end dates
    total_days = (end_date - start_date).days + 1

    # Determine the number of weekends within this period
    weekends = 0
    for i in range(total_days):
        date = start_date + datetime.timedelta(days=i)
        if date.weekday() >= 5:  # Saturday (5) or Sunday (6)
            weekends += 1

    # Determine the number of holidays within this period
    holiday_count = 0
    for holiday in holidays:
        if start_date <= holiday <= end_date:
            holiday_count += 1

    # Subtract the weekends and holidays from the total number of days
    weekdays = total_days - weekends - holiday_count

    # Set the number of weekdays to the maximum allowed weekdays if it exceeds it
    weekdays = min(weekdays, 30)

    # Return the number of weekdays as the result
    return weekdays