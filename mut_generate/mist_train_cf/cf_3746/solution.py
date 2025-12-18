"""
QUESTION:
Create a function `birth_dates_after_1990` that takes a list of tuples, where each tuple contains a name and a birth date in string format 'YYYY-MM-DD'. The function should return a dictionary where the birth dates are used as keys (stored as datetime objects) and the names are used as values, but only for individuals born after 1990.
"""

from datetime import datetime

def birth_dates_after_1990(data):
    birth_dates = {}
    for name, date_str in data:
        birth_date = datetime.strptime(date_str, "%Y-%m-%d")
        birth_dates[birth_date] = name
    return {date: name for date, name in birth_dates.items() if date.year > 1990}