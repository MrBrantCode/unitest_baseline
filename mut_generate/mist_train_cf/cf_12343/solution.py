"""
QUESTION:
Write a function named `convert_datetime` that takes a date and time string in the format "YYYY-MM-DD HH:MM:SS" as input and returns the date and time in the format "DD-MM-YYYY HH:MM". The function should handle potential errors that may occur during the conversion process and return an error message if the input string is in an invalid format.
"""

from datetime import datetime

def convert_datetime(datetime_str):
    try:
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        formatted_datetime = datetime_obj.strftime("%d-%m-%Y %H:%M")
        return formatted_datetime
    
    except ValueError:
        return "Invalid date and time format"