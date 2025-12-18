"""
QUESTION:
Write a function named `convert_time_zones` that takes a time in 12-hour format and a time zone offset as input. The function should convert the given time from Hawaiian Standard Time (HST) to East Africa Time (EAT) and return the converted time. Assume that East Africa Time is always a fixed offset from Hawaiian Standard Time.
"""

def convert_time_zones(time_hst, offset):
    """
    Converts a time in 12-hour format from Hawaiian Standard Time (HST) to East Africa Time (EAT).

    Args:
        time_hst (str): Time in 12-hour format (HH:MM AM/PM) in HST.
        offset (int): Time zone offset in hours.

    Returns:
        str: Converted time in 12-hour format (HH:MM AM/PM) in EAT.
    """
    hst_time_parts = time_hst.split()
    time_parts = hst_time_parts[0].split(':')
    hours, minutes = int(time_parts[0]), int(time_parts[1])
    am_pm = hst_time_parts[1]

    # Convert to 24-hour format for easier calculations
    if am_pm == 'PM' and hours != 12:
        hours += 12
    elif am_pm == 'AM' and hours == 12:
        hours = 0

    # Apply time zone offset
    hours += offset
    hours %= 24

    # Convert back to 12-hour format
    if hours == 0:
        hours = 12
        am_pm = 'AM'
    elif hours == 12:
        am_pm = 'PM'
    elif hours > 12:
        hours -= 12
        am_pm = 'PM'
    else:
        am_pm = 'AM'

    return f'{hours}:{minutes:02d} {am_pm}'