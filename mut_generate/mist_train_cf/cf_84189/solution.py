"""
QUESTION:
Construct two functions, `convert_date` and `convert_time`. 

`convert_date` should take a string date in the format "YYYY-MM-DD" and return a string in the format "Day, Date Month Year", where day is the actual day of the week and the month is represented in full. The function should handle invalid dates by returning an error message.

`convert_time` should take a string time in the format "HH:MM:SS" and return a string in the format "Hours: Minutes: Seconds AM/PM". The function should handle invalid times and time formats by returning an error message.
"""

import datetime

def convert_date(date_string):
    try:
        dt = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return dt.strftime("%A, %d %B %Y")
    except ValueError:
        return "Invalid date format, please use 'YYYY-MM-DD'"

def convert_time(time_string):
    try:
        dt = datetime.datetime.strptime(time_string, "%H:%M:%S")
        return dt.strftime("%I:%M:%S %p")
    except ValueError:
        return "Invalid time format, please use 'HH:MM:SS'"