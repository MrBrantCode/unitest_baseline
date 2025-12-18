"""
QUESTION:
Write a function called `avg_days_between_dates` that takes in an array of dates in the format 'mm/dd/yyyy' and a start and end date in the same format, and returns the average number of days between each date within that range. The function should return 0 if there are no dates in the range.
"""

from datetime import datetime, timedelta

def avg_days_between_dates(dates, start_date, end_date):
    # convert start and end date to datetime objects
    start_dt = datetime.strptime(start_date, '%m/%d/%Y')
    end_dt = datetime.strptime(end_date, '%m/%d/%Y')
    
    # filter dates within range and convert to datetime objects
    range_dates = [datetime.strptime(d, '%m/%d/%Y') for d in dates if start_dt <= datetime.strptime(d, '%m/%d/%Y') <= end_dt]
    
    # check if range has any dates
    if not range_dates:
        return 0
    
    # calculate total number of days between dates in range
    total_days = sum((range_dates[i+1] - range_dates[i]).days for i in range(len(range_dates)-1))
    
    # calculate average number of days
    avg_days = total_days / (len(range_dates) - 1)
    
    return round(avg_days, 1)