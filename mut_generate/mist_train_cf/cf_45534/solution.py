"""
QUESTION:
Create a function named `convert_date_format` that takes two parameters: a date string in the format 'dd/mm/yyyy' and a format type (1, 2, or 3). The function should convert the input date to the specified format and return it. The formats are: 
- 1: 'yyyy/mm/dd'
- 2: 'yyyy-mm-dd'
- 3: 'Month dd, yyyy' (Month is the full name of the month)

If the input date is invalid or the format type is not 1, 2, or 3, the function should return an error message 'Invalid date' or 'Invalid format type', respectively. The function should handle leap years correctly.
"""

from datetime import datetime

def convert_date_format(input_date, format_type = 1):
    try:
        #parse input date
        date_object = datetime.strptime(input_date, '%d/%m/%Y')
    except ValueError:
        return "Invalid date"

    # Convert date to desired format
    if format_type == 1:
        return date_object.strftime('%Y/%m/%d')
    elif format_type == 2:
        return date_object.strftime('%Y-%m-%d')
    elif format_type == 3:
        return date_object.strftime('%B %d, %Y')
    else:
        return "Invalid format type"