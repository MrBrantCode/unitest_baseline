"""
QUESTION:
Write a function named `count_business_days` that calculates the number of business days between a given start date and end date, excluding public holidays. The function should take three parameters: `start_date` and `end_date` as strings in the format 'YYYY-MM-DD', and `public_holidays` as a list of strings representing dates in the same format that should be excluded from the count.
"""

import pandas as pd

def count_business_days(start_date, end_date, public_holidays):
    """
    Calculate the number of business days between a given start date and end date, 
    excluding public holidays.

    Parameters:
    start_date (str): The start date in the format 'YYYY-MM-DD'.
    end_date (str): The end date in the format 'YYYY-MM-DD'.
    public_holidays (list): A list of strings representing dates in the same format 
        that should be excluded from the count.

    Returns:
    int: The number of business days between the start and end dates, excluding 
        public holidays.
    """

    # Create a date range
    dates = pd.bdate_range(start_date, end_date)

    # Exclude public holidays and weekends
    business_days = dates[~dates.isin(pd.to_datetime(public_holidays))]

    # Return the number of business days
    return len(business_days)