"""
QUESTION:
Create a function to format time data from a PostgreSQL table in Microsoft Access to display only the time component without the date. The function should take a time field as input and return the time in either "Short Time" or "Long Time" format. The function should be implementable in MS Access, possibly using a query.
"""

import datetime

def format_time(time_field):
    """
    Format time data from a PostgreSQL table in Microsoft Access to display only the time component without the date.

    Args:
        time_field (datetime.time): Time field from PostgreSQL table.

    Returns:
        str: Time in either "Short Time" or "Long Time" format.
    """
    return time_field.strftime("%I:%M %p")  # "Short Time" format
    # or
    # return time_field.strftime("%I:%M:%S %p")  # "Long Time" format