"""
QUESTION:
Write a function named `convert_cdt_to_est` that takes a time in the format HH:MM as input and returns the equivalent time in Eastern Standard Time, given that Central Daylight Time is 1 hour behind Eastern Standard Time.
"""

from datetime import datetime, timedelta

def convert_cdt_to_est(time_cdt):
    """
    Converts a time in Central Daylight Time (CDT) to Eastern Standard Time (EST).
    
    Args:
    time_cdt (str): Time in CDT in the format HH:MM
    
    Returns:
    str: Time in EST in the format HH:MM
    """
    # Parse the time from CDT
    time_cdt = datetime.strptime(time_cdt, '%H:%M')
    
    # Subtract 1 hour to convert to EST
    time_est = time_cdt - timedelta(hours=1)
    
    # Format the time back to HH:MM and return
    return time_est.strftime('%H:%M')