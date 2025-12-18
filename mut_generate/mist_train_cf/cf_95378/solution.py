"""
QUESTION:
Write a function `convert_to_iso8601_datetime(input_datetime)` that takes a string `input_datetime` as input, representing a date and time in any format (e.g., different date separators, different time formats), and returns the corresponding date and time in the ISO 8601 date format as a string, taking into account time zones, daylight saving time adjustments, and leap years.
"""

from datetime import datetime
from dateutil import parser

def convert_to_iso8601_datetime(input_datetime):
    # Step 1: Parse the input into components
    parsed_datetime = parser.parse(input_datetime)

    # Step 2 & 3: Normalize the components and Apply DST adjustments
    normalized_datetime = parsed_datetime.astimezone()

    # Step 4: Format the normalized components into ISO 8601
    iso8601_datetime = normalized_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")

    return iso8601_datetime