"""
QUESTION:
Create a function called `date_analyzer` that takes a string representing a date in either 'DD-MMM-YYYY' or 'DD-MM-YYYY' format and returns the date in 'weekday, month day, year' format if the date is valid, otherwise returns an error message. The function should use the Gregorian calendar, where the week starts from Monday and ends on Sunday.
"""

from datetime import datetime

def date_analyzer(date_string):
    try:
        date = datetime.strptime(date_string, '%d %b %Y') 
    except ValueError:
        try:
            date = datetime.strptime(date_string, '%d-%m-%Y')  
        except ValueError:
            return "Error: invalid format."
        else:
            return datetime.strftime(date, '%A, %B %d, %Y')
    else:
        return datetime.strftime(date, '%A, %B %d, %Y')