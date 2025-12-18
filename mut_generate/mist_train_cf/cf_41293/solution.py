"""
QUESTION:
Write a function `convert_date_time_format(input_datetime: str) -> str` that takes a date and time string in either `"%Y-%m-%dT%H:%M:%SZ"` or `"%Y-%m-%dT%H:%M:%S.%fZ"` format and returns the converted date and time string in the opposite format, preserving the time zone information. The input date and time strings will always be valid and in the specified formats.
"""

from datetime import datetime

def convert_date_time_format(input_datetime: str) -> str:
    DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
    DATE_TIME_FORMAT_FRACTIONAL = "%Y-%m-%dT%H:%M:%S.%fZ"

    if 'Z' not in input_datetime:
        input_datetime += 'Z'
        
    if '.' in input_datetime:
        input_format = DATE_TIME_FORMAT_FRACTIONAL
        output_format = DATE_TIME_FORMAT
    else:
        input_format = DATE_TIME_FORMAT
        output_format = DATE_TIME_FORMAT_FRACTIONAL

    dt = datetime.strptime(input_datetime, input_format)
    return dt.strftime(output_format)