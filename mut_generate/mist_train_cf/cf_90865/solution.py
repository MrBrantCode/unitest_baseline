"""
QUESTION:
Write a function `get_business_days` that takes in three parameters: `start_date`, `end_date`, and an optional list of `holidays`. The function should calculate and return the number of business days between `start_date` and `end_date`, excluding weekends and public holidays.
"""

import datetime

def get_business_days(start_date, end_date, holidays=[]):
    days = (end_date - start_date).days + 1
    business_days = 0
    
    for i in range(days):
        date = start_date + datetime.timedelta(days=i)
        if date.weekday() < 5 and date not in holidays:
            business_days += 1
    
    return business_days