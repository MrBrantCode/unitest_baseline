"""
QUESTION:
Write a function named `working_days` that calculates the number of working days between two given dates, excluding weekends and holidays. The function should also consider custom company holidays and half working days. It must accommodate different time zones and handle dates as timezone-aware datetime objects. The function should take the following parameters: `start_date`, `end_date`, `holidays`, `half_days`, and `tz`. It should return the total number of working days as a float, with half days counting as 0.5 days.
"""

import pandas as pd

def working_days(start_date, end_date, holidays, half_days, tz):
    # Convert string to datetime object and set timezone information
    start_date = pd.to_datetime(start_date).tz_localize(tz)
    end_date = pd.to_datetime(end_date).tz_localize(tz)

    # Initialize counter for working days
    total_days = 0
    
    # Loop through each date from start to end
    for single_date in pd.date_range(start=start_date, end=end_date):
        # Exclude weekends
        if single_date.weekday() < 5:            
            # If it's a half day, count as 0.5; if it's a holiday, count as 0
            if single_date in half_days:
                total_days += 0.5
            elif single_date not in holidays:
                total_days += 1          
    
    return total_days