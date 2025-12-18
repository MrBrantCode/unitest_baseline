"""
QUESTION:
Given a date string in the format "dd/mm/yyyy", write a function `find_day_of_week` that takes the date string as input and returns the corresponding day of the week as a string. The input date string will always be valid.
"""

def find_day_of_week(date_string):
    day = int(date_string[0:2])
    month = int(date_string[3:5])
    year = int(date_string[6:])
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    import datetime
    date = datetime.datetime(year, month, day)
    return date.strftime("%A")