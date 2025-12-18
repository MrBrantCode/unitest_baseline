"""
QUESTION:
Create a function `parse_dates` that takes a list of timestamps in various unstandardized string formats, parses and standardizes them into 'Day-Month-Year Hours:Minutes' format, and returns the list of parsed dates. 

Additionally, create a function `get_differences` that calculates the time difference in minutes between each consecutive timestamp in the series and returns the list of time differences.

The solution should have a time complexity of O(n), where n is the number of timestamps.
"""

from dateutil.parser import parse
from datetime import datetime

def parse_dates(date_strings):
    parsed_dates = [parse(date) for date in date_strings]
    return [date.strftime('%d-%m-%Y %H:%M') for date in parsed_dates]

def get_differences(dates):
    parsed_dates = [parse(date) for date in dates]
    differences = []
    for i in range(1, len(parsed_dates)):
        diff = parsed_dates[i] - parsed_dates[i-1]
        differences.append(int(diff.total_seconds() / 60))  # convert to minutes
    return differences