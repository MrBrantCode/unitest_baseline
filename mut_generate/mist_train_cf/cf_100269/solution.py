"""
QUESTION:
Combine consecutive dates in a set into date ranges, separated by commas, where single dates are comma-separated and date ranges are formatted as "start to end". 

Create a function called combine_dates that takes a set of dates as input and returns a string of combined dates.
"""

from datetime import datetime, timedelta

def combine_dates(date_set):
    date_list = sorted(date_set)
    combined_dates = []
    start_date = date_list[0]
    end_date = start_date
    
    for i in range(1, len(date_list)):
        curr_date = date_list[i]
        if curr_date - end_date == timedelta(days=1):
            end_date = curr_date
        else:
            combined_dates.append((start_date, end_date))
            start_date = end_date = curr_date
    
    combined_dates.append((start_date, end_date))
    
    result = ''
    
    for start, end in combined_dates:
        if start == end:
            result += start.strftime('%Y-%m-%d') + ','
        else:
            result += start.strftime('%Y-%m-%d') + ' to ' + end.strftime('%Y-%m-%d') + ','
    
    return result[:-1]