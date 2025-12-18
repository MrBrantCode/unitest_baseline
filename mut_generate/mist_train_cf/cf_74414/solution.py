"""
QUESTION:
Write a function that converts a server timestamp to a user's local timezone. The function should take in a timestamp and the user's timezone offset as arguments and return the timestamp in the user's local timezone. Assume the server is in the UTC-0700 timezone and that the user's timezone is provided in the format '-04:00'.
"""

from datetime import datetime, timedelta

def convert_server_timestamp_to_local(timestamp, timezone_offset):
    # Convert the timezone offset to hours and minutes
    offset_hours, offset_minutes = map(int, timezone_offset.split(':'))
    
    # Calculate the total offset in minutes
    total_offset_minutes = offset_hours * 60 + offset_minutes
    
    # Calculate the server's offset in minutes (UTC-0700)
    server_offset_minutes = -7 * 60
    
    # Convert the server timestamp to the user's local timezone
    local_timestamp = timestamp + timedelta(minutes=total_offset_minutes - server_offset_minutes)
    
    return local_timestamp