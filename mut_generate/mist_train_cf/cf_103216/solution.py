"""
QUESTION:
Write a function `days_between_dates` that calculates the number of days between two given dates, considering leap years. The input dates are in the format "day month year" (e.g., "12 03 2021"). The function should return the absolute difference in days between the two dates.
"""

import calendar

def days_between_dates(first_date, second_date):
    # Split the dates into day, month, and year
    first_day, first_month, first_year = map(int, first_date.split(' '))
    second_day, second_month, second_year = map(int, second_date.split(' '))
    
    # Calculate the number of days between the two dates
    start_date = (first_year, first_month, first_day)
    end_date = (second_year, second_month, second_day)
    days = abs((end_date[0] - start_date[0]) * 365 + (end_date[1] - start_date[1]) * 30 + end_date[2] - start_date[2])
    
    # calculate the remaining days for the months in between years and months
    for year in range(min(start_date[0], end_date[0]), max(start_date[0], end_date[0])):
        if calendar.isleap(year):
            days += 1
            
    for month in range(min(start_date[1], end_date[1]), max(start_date[1], end_date[1])):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days += 1
        elif month == 2:
            if calendar.isleap(min(start_date[0], end_date[0])):
                days += 1
        else:
            days += 0
    
    return days