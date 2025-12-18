"""
QUESTION:
Create a function named `cet_to_utc` that takes a date and time string in the format "DD-MM-YYYY 11:45 PM" in Central European Time (CET) and returns the corresponding date and time in Coordinated Universal Time (UTC) in the same format. The function should use the pytz module for timezone conversions.
"""

from datetime import datetime
import pytz

def cet_to_utc(date_time_str):
    # Convert date_time_str to datetime object
    date_time_obj = datetime.strptime(date_time_str, "%d-%m-%Y %I:%M %p")
    
    # Localize the datetime object to CET timezone
    cet_tz = pytz.timezone('CET')
    date_time_obj = cet_tz.localize(date_time_obj)
    
    # Convert to UTC timezone
    utc_tz = pytz.UTC
    date_time_obj = date_time_obj.astimezone(utc_tz)
    
    # Return date and time in UTC in the format "DD-MM-YYYY 11:45 PM"
    return date_time_obj.strftime("%d-%m-%Y %I:%M %p")