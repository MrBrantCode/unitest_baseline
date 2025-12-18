"""
QUESTION:
Develop a function `day_type_and_next_public_holiday` that takes a date string in the ISO 8601 standard format (YYYY-MM-DD) and returns the day of the week, whether it's a weekday or weekend, and the number of days remaining until the next public holiday. The public holidays to consider are New Year's Day (January 1st), Independence Day (July 4th), and Christmas (December 25th).
"""

from datetime import datetime, timedelta

# list of US public holidays
public_holidays = ["01-01", "07-04", "12-25"]

def day_type_and_next_public_holiday(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_week = date_obj.strftime('%A')

    # check if it's a weekday or weekend
    if day_of_week in ['Saturday', 'Sunday']:
        day_type = 'Weekend'
    else:
        day_type = 'Weekday'

    # calculate days remaining until the next public holiday
    remaining_days_list = []
    for holiday in public_holidays:
        holiday_date_str = f'{date_obj.year}-{holiday}'
        holiday_date_obj = datetime.strptime(holiday_date_str, '%Y-%m-%d')

        # if the holiday has already passed this year, consider next year's date
        if holiday_date_obj < date_obj:
            holiday_date_str = f'{date_obj.year + 1}-{holiday}'
            holiday_date_obj = datetime.strptime(holiday_date_str, '%Y-%m-%d')

        remaining_days = (holiday_date_obj - date_obj).days
        remaining_days_list.append(remaining_days)

    # returns the minimum number of days to the next holiday
    remaining_days_to_next_holiday = min(remaining_days_list)

    return day_of_week, day_type, remaining_days_to_next_holiday