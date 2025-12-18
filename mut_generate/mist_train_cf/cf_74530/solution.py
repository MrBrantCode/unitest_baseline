"""
QUESTION:
Create a function `convertToISO` that takes a list of date strings in human-readable format, converts them into the standardized ISO 8601 format, and returns the converted dates as a list of strings. If a date is in an invalid or unrecognized format, append an error message in the format 'Invalid date: <original date string>' to the result list instead.
"""

from dateutil.parser import parse
from datetime import datetime

def convertToISO(dates):
    iso_dates = []
    for date in dates:
        try:
            # Try converting the date to datetime object then to ISO 8601
            iso_dates.append(parse(date).strftime('%Y-%m-%d'))
        except ValueError:
            # If conversion fails, append error message
            iso_dates.append(f'Invalid date: {date}')
    return iso_dates