"""
QUESTION:
Develop a function `get_day_name_and_holiday` that takes a date string in the format 'YYYY-MM-DD' as an argument, representing a date between January 1st, 1900 and December 31st, 2099. The function should return the day name of the given date and check if the date is a public holiday in a specific country, printing the corresponding holiday name if applicable. The function should account for leap years and handle invalid date formats.
"""

import datetime

def get_day_name_and_holiday(date):
    try:
        day_name = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")
        year, month, day = map(int, date.split("-"))
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        holidays = {
            "United States": {
                (1, 1): "New Year's Day",
                (7, 4): "Independence Day",
                (12, 25): "Christmas Day"
            },
            "United Kingdom": {
                (1, 1): "New Year's Day",
                (12, 25): "Christmas Day",
                (12, 26): "Boxing Day"
            }
            # Add more countries and their public holidays here
        }

        country = "United States"  # Replace with the desired country

        if (month, day) in holidays.get(country, {}):
            holiday_name = holidays[country][(month, day)]
            return f"{day_name}, {date} is a public holiday in {country}: {holiday_name}"
        else:
            return f"{day_name}, {date} is not a public holiday in {country}"

    except ValueError:
        return "Invalid date format. Please use the format 'YYYY-MM-DD'."