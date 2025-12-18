"""
QUESTION:
Convert the dates in a given string from the format 'dd/mm/yyyy' to 'mm/dd/yyyy' using regex, ensuring the input string contains only valid dates. The function should be efficient and handle a large number of dates (up to 100,000) while considering edge cases such as leap years, different lengths for months and days, and different date separators. If an invalid date is encountered, the function should either raise an error or skip that particular date.
"""

import re

def entance(input_string):
    date_pattern = r'(?:\b|/)(0[1-9]|[1-2][0-9]|3[0-1])(/)(0[1-9]|1[0-2])/\b([0-9]{4})\b'

    converted_dates = []
    matches = re.findall(date_pattern, input_string)

    for match in matches:
        day, separator, month, year = match
        converted_date = f'{month}{separator}{day}{separator}{year}'
        converted_dates.append(converted_date)

    return converted_dates