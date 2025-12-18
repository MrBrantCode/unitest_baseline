"""
QUESTION:
Write a function `translate_time_zones` that takes the time (in 24-hour format) in Eastern Standard Time (EST) as input and returns its corresponding time in Australian Central Standard Time (ACST), considering ACST is 14.5 hours ahead of EST. Note that the solution should handle cases where the translated time falls on the next day.
"""

from datetime import datetime, timedelta

def translate_time_zones(est_time):
    """
    Translate the time (in 24-hour format) from Eastern Standard Time (EST) to Australian Central Standard Time (ACST).

    Args:
    est_time (str): Time in 24-hour format (HH:MM) in EST.

    Returns:
    str: Corresponding time in ACST.
    """
    # Split the time into hours and minutes
    hours, minutes = map(int, est_time.split(':'))
    
    # Create a datetime object
    est_datetime = datetime(1, 1, 1, hours, minutes)
    
    # Calculate the time difference between EST and ACST (14.5 hours)
    time_diff = timedelta(hours=14, minutes=30)
    
    # Add the time difference to the EST time
    acst_datetime = est_datetime + time_diff
    
    # Format the ACST time
    acst_time = acst_datetime.strftime('%H:%M')
    
    # If the translated time falls on the next day, add ' (next day)' to the result
    if acst_datetime.day > est_datetime.day:
        acst_time += ' (next day)'
    
    return acst_time