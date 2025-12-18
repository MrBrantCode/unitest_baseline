"""
QUESTION:
Create a function `combine_dates` that takes a string of dates separated by commas as input and returns a string where consecutive dates are combined into date ranges in the format "2022-01-01 to 2022-01-05". The input dates are in the format "YYYY-MM-DD" and the output should be a comma-separated string of date ranges.
"""

from datetime import datetime, timedelta

def combine_dates(date_str):
    # Convert input string into list of datetime objects
    dates = sorted([datetime.strptime(d, "%Y-%m-%d") for d in date_str.split(",")])
    
    # Initialize variables for tracking consecutive date ranges
    start_date = None
    end_date = None
    ranges = []
    
    # Loop through dates and build date ranges
    for date in dates:
        if end_date is None:
            # This is the first date in a new range
            start_date = date
            end_date = date
        elif date == end_date + timedelta(days=1):
            # This date is consecutive with the previous date, so extend the range
            end_date = date
        else:
            # This date is not consecutive, so add the previous range to the list and start a new one
            ranges.append((start_date, end_date))
            start_date = date
            end_date = date
    
    # Add the final range to the list (if any)
    if start_date is not None:
        ranges.append((start_date, end_date))
    
    # Convert each range to a string and join them with commas
    return ", ".join([f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}" 
                      if start_date != end_date 
                      else start_date.strftime('%Y-%m-%d')
                      for start_date, end_date in ranges])