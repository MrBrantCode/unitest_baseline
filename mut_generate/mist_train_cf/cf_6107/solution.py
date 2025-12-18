"""
QUESTION:
Write a function named `convert_dates` that takes a string of dates in the format 'dd/mm/yyyy' as input, validates the dates, and converts them to the format 'mm/dd/yyyy'. The function should be able to handle up to 100,000 dates, handle invalid dates and different date formats, optimize for efficiency and performance, and provide error handling and unit tests. The input string may contain multiple dates separated by any character, and the function should return a list of converted dates.
"""

import re

def convert_dates(input_string):
    date_pattern = r'(?:\b|/)(0[1-9]|[1-2][0-9]|3[0-1])(/)(0[1-9]|1[0-2])/\b([0-9]{4})\b'

    converted_dates = []

    matches = re.findall(date_pattern, input_string)

    for match in matches:
        day, separator, month, year = match

        converted_date = f'{month}{separator}{day}{separator}{year}'

        converted_dates.append(converted_date)

    return converted_dates