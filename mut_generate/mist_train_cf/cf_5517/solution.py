"""
QUESTION:
Write a function `hours_since_1970` that calculates the number of hours elapsed since January 1st, 1970, until a given date in the format "dd-mm-yyyy". The function should take into account leap years and return the total number of hours as the result. The input date will always be in a valid format.
"""

from datetime import datetime

def hours_since_1970(date_string):
    # Parse the given date string
    date = datetime.strptime(date_string, "%d-%m-%Y")

    # Calculate the difference between the given date and January 1st, 1970
    delta = date - datetime(1970, 1, 1)

    # Return the total number of hours
    return delta.total_seconds() / 3600