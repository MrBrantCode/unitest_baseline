"""
QUESTION:
Create a function `calculate_period` that takes a list of dates in the format 'YYYY-MM-DD' and returns the average period between them in days. The function should handle a list of at least two dates and assume that the dates are in chronological order.
"""

import datetime

def calculate_period(dates):
    periods = []
    for i in range(len(dates)-1):
        d1 = datetime.datetime.strptime(dates[i], '%Y-%m-%d')
        d2 = datetime.datetime.strptime(dates[i+1], '%Y-%m-%d')
        delta = d2 - d1
        periods.append(delta.days)
    avg_period = sum(periods) / len(periods)
    return avg_period