"""
QUESTION:
Function Name: Not specified

Write a function that calculates the number of business days (excluding weekends and public holidays) between two given dates. The function should correctly handle time zones and daylight saving time changes.
"""

def calculate_business_days(start_date, end_date):
    """
    Calculate the number of business days between two given dates, excluding weekends and public holidays.

    Args:
    start_date (datetime): The start date.
    end_date (datetime): The end date.

    Returns:
    int: The number of business days.
    """

    import pandas as pd
    from pandas.tseries.holiday import USFederalHolidayCalendar
    from pandas.tseries.offsets import CustomBusinessDay

    # Define the business day frequency with custom holidays
    cal = USFederalHolidayCalendar()
    custom_bday = CustomBusinessDay(holidays=cal.holidays(start=start_date, end=end_date))

    # Generate the business days between the start and end dates
    business_days = pd.date_range(start=start_date, end=end_date, freq=custom_bday)

    # Return the number of business days
    return len(business_days)