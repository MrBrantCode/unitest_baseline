"""
QUESTION:
Write a function named `count_weekdays` that takes two parameters, `start_date` and `end_date`, both in the format DD MMM YYYY. The function should return the number of weekdays (Monday to Friday) between `start_date` and `end_date`, excluding weekends and public holidays. 

The function should handle leap years and public holidays that are fixed dates, but may be observed every year. The public holidays can be defined as a dictionary where the keys are the dates and the values are the holiday names. The function should also validate the input dates to ensure they are in the correct format and order.
"""

import datetime

def count_weekdays(start_date, end_date):
    # Define a dictionary of public holidays with fixed dates
    public_holidays = {
        datetime.date(2020, 1, 1): "New Year's Day",
        datetime.date(2020, 5, 1): "Labour Day",
        datetime.date(2020, 12, 25): "Christmas Day"
    }

    # Validate input dates
    try:
        start_date = datetime.datetime.strptime(start_date, "%d %b %Y").date()
        end_date = datetime.datetime.strptime(end_date, "%d %b %Y").date()
    except ValueError:
        print("Invalid date format. Please use DD MMM YYYY format.")
        return

    if start_date > end_date:
        print("Start date cannot be after end date.")
        return

    # Calculate number of days between the two dates
    total_days = (end_date - start_date).days + 1

    # Count the number of weekdays and exclude weekends and public holidays
    weekdays = 0
    for i in range(total_days):
        current_date = start_date + datetime.timedelta(days=i)

        # Exclude weekends (Saturday = 5, Sunday = 6)
        if current_date.weekday() < 5:
            # Exclude public holidays
            if current_date not in public_holidays:
                weekdays += 1

    return weekdays