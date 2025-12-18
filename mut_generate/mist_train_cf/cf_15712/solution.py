"""
QUESTION:
Write a function named `count_business_days` that calculates the number of business days (excluding weekends and public holidays) between two given dates, taking into account time zones and daylight saving time changes. The function should accept two datetime objects as input, `start_date` and `end_date`, with their respective time zones, and return the number of business days. Consider US federal holidays as public holidays for this calculation.
"""

import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

def count_business_days(start_date, end_date):
    """
    Calculate the number of business days between two dates, 
    excluding weekends and public holidays, considering time zones and daylight saving time changes.

    Args:
        start_date (datetime): The start date.
        end_date (datetime): The end date.

    Returns:
        int: The number of business days between the start and end dates.
    """

    # Define the business day frequency with custom holidays
    cal = USFederalHolidayCalendar()
    custom_bday = CustomBusinessDay(holidays=cal.holidays(start=start_date, end=end_date))

    # Generate the business days between the start and end dates
    business_days = pd.date_range(start=start_date, end=end_date, freq=custom_bday)

    # Return the number of business days
    return len(business_days)