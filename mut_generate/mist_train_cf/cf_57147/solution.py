"""
QUESTION:
Write a function `shift_time_to_nzst` that takes a time in London GMT (HH:MM AM/PM) and returns the corresponding time in New Zealand Standard Time (NZST), which is 12 hours ahead of GMT.
"""

from datetime import datetime, timedelta

def shift_time_to_nzst(time_in_london_gmt):
    """
    This function shifts the given London GMT time to New Zealand Standard Time (NZST).
    
    Args:
        time_in_london_gmt (str): The time in London GMT in the format 'HH:MM AM/PM'
    
    Returns:
        str: The corresponding time in New Zealand Standard Time (NZST)
    """
    
    # Split the input string into hours, minutes and AM/PM
    time_in_london_gmt_parts = time_in_london_gmt.split()
    time_parts = time_in_london_gmt_parts[0].split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    am_pm = time_in_london_gmt_parts[1]
    
    # Convert to 24 hour format
    if am_pm == 'PM' and hours != 12:
        hours += 12
    elif am_pm == 'AM' and hours == 12:
        hours = 0
    
    # Create a datetime object
    london_time = datetime(2024, 1, 1, hours, minutes)
    
    # Add 12 hours to get the NZST time
    nzst_time = london_time + timedelta(hours=12)
    
    # Format the NZST time
    nzst_time_string = nzst_time.strftime('%I:%M %p')
    
    return nzst_time_string