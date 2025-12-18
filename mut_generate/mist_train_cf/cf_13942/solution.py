"""
QUESTION:
Create a Python function named `store_and_convert_year` that takes two parameters: an integer `year` and a string `new_format`. The function should store the given year in ISO 8601 format and then convert the stored ISO 8601 date to the specified `new_format`. The function should return the converted date string. 

The input `year` will be a four-digit integer representing a year, and the `new_format` will be a string specifying the desired date format (e.g., 'mm-dd-yyyy'). The ISO 8601 date should have the day and month as '01' since only the year is given. The function should handle the conversion correctly, considering the 'mm-dd-yyyy' format as an example.
"""

from datetime import datetime

def store_and_convert_year(year, new_format):
    # Storing year in ISO 8601 format
    iso_format = datetime(year=year, month=1, day=1).isoformat()
    
    # Converting date format
    datetime_obj = datetime.fromisoformat(iso_format)
    new_date_format = datetime_obj.strftime(new_format.replace('yyyy', '%Y').replace('mm', '%m').replace('dd', '%d'))
    return new_date_format