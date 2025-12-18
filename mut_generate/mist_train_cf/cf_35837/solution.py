"""
QUESTION:
Write a function `convertDateFormat` that takes a string `date` in the format "dd/mm/yyyy" and returns a string in the format "Month dd, yyyy". The function should handle valid date strings and return the converted format, or return "Invalid date" for invalid date strings. The output month should be in title case and the function should handle leap years and invalid dates appropriately.
"""

from datetime import datetime

def convertDateFormat(date):
    try:
        date_obj = datetime.strptime(date, '%d/%m/%Y')
        return date_obj.strftime('%B %d, %Y')
    except ValueError:
        return "Invalid date"