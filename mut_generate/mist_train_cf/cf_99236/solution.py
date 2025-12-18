"""
QUESTION:
Write a function called `process_production_log` that takes a list of dictionaries representing a production log, where each dictionary contains 'entry', 'start_time', and 'end_time' keys, and a time zone offset as input. The function should convert the 'start_time' and 'end_time' from UTC to the local time zone, calculate the time difference in minutes and seconds, and return the result for each entry. The 'start_time' and 'end_time' are in ISO 8601 format and the time zone offset is a timedelta object. The function should handle multiple entries in the production log.
"""

import datetime

def process_production_log(production_log, time_zone_offset):
    """
    Process a production log by converting the 'start_time' and 'end_time' from UTC to the local time zone,
    calculating the time difference in minutes and seconds, and returning the result for each entry.

    Args:
        production_log (list): A list of dictionaries representing the production log.
        time_zone_offset (datetime.timedelta): The time zone offset.

    Returns:
        list: A list of dictionaries containing the entry, start time, end time, time difference in minutes, and time difference in seconds.
    """
    result = []
    for entry in production_log:
        # Convert the start and end times to UTC timestamps
        start_time_utc = datetime.datetime.fromisoformat(entry["start_time"]).replace(tzinfo=datetime.timezone.utc)
        end_time_utc = datetime.datetime.fromisoformat(entry["end_time"]).replace(tzinfo=datetime.timezone.utc)
        
        # Convert the UTC timestamps to local timestamps
        start_time_local = start_time_utc + time_zone_offset
        end_time_local = end_time_utc + time_zone_offset
        
        # Calculate the time difference in minutes
        time_difference_minutes = (end_time_local - start_time_local).total_seconds() / 60
        
        # Store the result
        result.append({
            "entry": entry["entry"],
            "start_time": start_time_local.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": end_time_local.strftime("%Y-%m-%d %H:%M:%S"),
            "time_difference_minutes": int(time_difference_minutes),
            "time_difference_seconds": int((time_difference_minutes % 1) * 60)
        })
    
    return result