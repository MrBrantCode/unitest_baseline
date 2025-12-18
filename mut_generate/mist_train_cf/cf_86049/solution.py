"""
QUESTION:
Create a function named `validate_parse_display` that takes a string representing a date as input and attempts to parse it in the following formats: DD-MMM-YYYY, DD/MM/YYYY, DD MMM YYYY, and DD MM YYYY. If the date string can be successfully parsed, the function should print the date components (day, month, and year). If the date string cannot be parsed in any of the supported formats, the function should print an error message. The function should also handle leap years and numeric month representations.
"""

import datetime

def validate_parse_display(date_string):
    valid_formats = ['%d-%b-%Y', '%d/%m/%Y', '%d %b %Y', '%d %m %Y']
    
    for date_format in valid_formats:
        try:
            parsed_date = datetime.datetime.strptime(date_string, date_format)
            print(f"Parsed Date: Day-{parsed_date.day}, Month-{parsed_date.month}, Year-{parsed_date.year}")
            return
        except ValueError:
            pass

    print('Invalid date entry. Please ensure the date follows format DD-MMM-YYYY.')