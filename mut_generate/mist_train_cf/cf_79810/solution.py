"""
QUESTION:
Write a function `convert_to_hst` that takes a time string in the format "HH:MM" representing the time in Indian Standard Time (IST) and returns the equivalent time in Hawaii Standard Time (HST). IST is 15 hours and 30 minutes ahead of HST, and the function should account for date changes if necessary.
"""

from datetime import datetime, timedelta

def convert_to_hst(ist_time):
    """
    Converts a time string from Indian Standard Time (IST) to Hawaii Standard Time (HST).
    
    Args:
        ist_time (str): Time in IST format "HH:MM".
    
    Returns:
        str: Time in HST format "HH:MM".
    """
    
    # Convert IST time string to datetime object
    ist_datetime = datetime.strptime(ist_time, "%H:%M")
    
    # Calculate the time difference between IST and HST (15 hours 30 minutes)
    time_diff = timedelta(hours=15, minutes=30)
    
    # Subtract the time difference from IST datetime object
    hst_datetime = ist_datetime - time_diff
    
    # If the resulting time is on the previous day, adjust the date accordingly
    if hst_datetime.day < ist_datetime.day:
        hst_datetime += timedelta(days=1)
    
    # Format the HST datetime object back to time string
    hst_time = hst_datetime.strftime("%H:%M")
    
    return hst_time