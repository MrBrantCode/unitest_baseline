"""
QUESTION:
Write a function called `reformat_date` that takes a string representing a date in the format "day month year" (e.g. "20th Oct 2052") and returns a string representing the date in the format "year-month-day, weekday" (e.g. "2052-10-20, Tuesday"). The function should handle dates where the day is either one or two digits.
"""

from datetime import datetime

def reformat_date(date):
    # Mapping the month's name to its number
    month_map = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
        'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    }

    # Splitting the date into its three components
    day, month, year = date.split(' ')

    # Removing the last two characters of the day (st, nd, rd, th)
    day = day[:-2]
    if len(day) == 1:
        day = '0' + day

    # Fetching the corresponding month number
    month = month_map[month]

    # Getting the formatted date
    formatted_date = str(year) + '-' + month + '-' + day
    date_object = datetime.strptime(formatted_date, '%Y-%m-%d')

    # List of days for the weekday() function
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return formatted_date + ", " + days[date_object.weekday()]