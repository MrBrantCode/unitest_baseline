"""
QUESTION:
The function name is `get_business_days`. It should take three parameters: `start_date`, `end_date`, and an optional list of `holidays`. The function should calculate and return the number of business days between `start_date` and `end_date` (inclusive), excluding weekends and public holidays. The dates should be in the format of `datetime.date` objects.
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