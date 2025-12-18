"""
QUESTION:
Write a function named `number_of_working_days` that calculates the number of working days between two given dates, excluding weekends and holidays. The function takes three parameters: `start_date`, `end_date`, and `holidays`. The `start_date` and `end_date` should be in a format that can be converted to a date object, and `holidays` should be a list of dates in the same format. The function should return the number of working days between `start_date` and `end_date`, inclusive. The function should assume that the input dates are valid and the `start_date` is not later than the `end_date`.
"""

import numpy as np

def number_of_working_days(start_date, end_date, holidays):
    """
    Calculate the number of working days between two dates
    :param start_date: The start date
    :param end_date: The end date
    :param holidays: The list of holiday dates
    :return: The number of working days between the two dates
    """

    # Make sure the start date is not greater than the end date
    if start_date > end_date:
        return "Start date must be earlier than end date"

    # Convert the dates to numpy datetime64 objects
    start_date = np.datetime64(start_date, 'D')
    end_date = np.datetime64(end_date, 'D')

    # Add one to the end date to make it inclusive 
    end_date = end_date + np.timedelta64(1, 'D')

    # Create an array of weekdays between start and end date
    weekdays = np.arange(start_date, end_date, dtype='datetime64[D]')

    # Create an array of weekends
    weekends = np.is_busday(weekdays, weekmask='Mon Tue Wed Thu Fri')

    # Create an array of holidays
    holidays = np.isin(weekdays, np.array(holidays, dtype='datetime64[D]'))

    # Calculate the number of business days
    business_days = weekdays[weekends & ~holidays].size

    return business_days