"""
QUESTION:
Write a function `convert_time_format(times, offset)` that takes a list of time strings in 24-hour format (`times`) and a time zone offset (`offset`) as input, and returns a list of time strings in 12-hour format based on the given time zone offset. The function should handle cases where the offset causes the time to go past midnight. The output time strings should be in the format "HH:MM AM/PM", where HH represents the hour in 12-hour format, MM represents the minute, and AM/PM indicates whether the time is in the morning or afternoon.
"""

def convert_time_format(times, offset):
    converted_times = []
    
    for time in times:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        
        new_hours = hours + offset
        
        if new_hours < 0:
            new_hours += 24
        elif new_hours >= 24:
            new_hours -= 24
        
        if new_hours >= 12:
            indicator = "PM"
            if new_hours > 12:
                new_hours -= 12
        else:
            indicator = "AM"
            if new_hours == 0:
                new_hours = 12
        
        new_time = "{}:{:02d} {}".format(new_hours, minutes, indicator)
        converted_times.append(new_time)
    
    return converted_times