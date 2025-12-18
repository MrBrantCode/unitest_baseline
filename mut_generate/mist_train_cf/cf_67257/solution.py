"""
QUESTION:
Write a function named `parse_date` that takes a date string as input, parses it, and returns a string displaying the day, month, and year. The function should support the following formats: DD-MM-YYYY, DD/MM/YYYY, DD MMM YYYY (where MMM is the written month), and automatically convert the input to DD-MM-YYYY. It must handle leap years, edge cases, and invalid dates, and raise an error for invalid inputs.
"""

from datetime import datetime

def parse_date(date_string):
    # A dictionary to map month names to their numeric values
    month_to_num = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
                    'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
                    'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

    # Try to convert the given date string to a datetime object
    try:

        # If the input is already of the format 'DD-MM-YYYY'
        if '-' in date_string:
            date_components = date_string.split('-')
            
            if date_components[1].isdigit():
                date = datetime.strptime(date_string, '%d-%m-%Y')
            else:
                date_components[1] = str(month_to_num[date_components[1].lower()])
                date = datetime.strptime('-'.join(date_components), '%d-%m-%Y')
        
        # If the input is of the format 'DD/MM/YYYY'
        elif '/' in date_string:
            date_components = date_string.split('/')
            date = datetime.strptime(date_string, '%d/%m/%Y')

        # If the input is of the format 'DD MMM YYYY'
        else:
            date_components = date_string.split(' ')
            date_components[1] = str(month_to_num[date_components[1].lower()])
            date = datetime.strptime(' '.join(date_components), '%d %m %Y')

    except ValueError:
        return 'The given date string is not valid.'

    # Display the date
    return 'The day is {0:02d}.\nThe month is {1:02d}.\nThe year is {2}.'.format(date.day, date.month, date.year)