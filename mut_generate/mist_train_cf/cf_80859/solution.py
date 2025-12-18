"""
QUESTION:
Create a function named `organize_timestamps` that takes a list of timestamps in 24-hour format (HH:MM) as input. The function should convert each valid timestamp to 12-hour format (HH:MM AM/PM), sort the timestamps in chronological order, and identify any invalid timestamps. Invalid timestamps should be labeled as "Invalid Time". The function should return a list of sorted, converted timestamps, with invalid timestamps included.
"""

from datetime import datetime

def organize_timestamps(timestamps):
    """Organize and convert a list of timestamps"""
    timestamp_dict = {}
    for time in timestamps:
        try:
            in_time = datetime.strptime(time, "%H:%M")
            timestamp_dict[in_time] = time
        except ValueError:
            timestamp_dict[datetime.max] = time  # store invalid time with max datetime
            
    sorted_times = [v for k, v in sorted(timestamp_dict.items())]
    
    converted_times = []
    for time in sorted_times:
        try:
            in_time = datetime.strptime(time, "%H:%M")
            out_time = datetime.strftime(in_time, "%I:%M %p")
            converted_times.append(out_time)
        except ValueError:
            converted_times.append("Invalid Time")
            
    return converted_times