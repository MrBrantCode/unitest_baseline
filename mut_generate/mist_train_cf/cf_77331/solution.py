"""
QUESTION:
Write a function `convert_to_ist` that takes a string representing a time in Greenwich Mean Time (GMT) and returns the corresponding time in Indian Standard Time (IST). The function should handle different input time formats (e.g., '6:00', '6am', '06:00:00', etc.) and invalid inputs, but does not need to consider daylight savings. The IST time should be returned as a string in the format 'HH:MM AM/PM' or a similar 12-hour format.
"""

from datetime import datetime as dt, timedelta as td

def convert_to_ist(gmt):
    try:
        # Consider multiple possible time string formats
        for fmt in ('%I:%M %p', '%H:%M', '%H:%M:%S'):
            try:
                gmt = dt.strptime(gmt, fmt)
                break
            except ValueError:
                pass

        # GMT to IST conversion (IST = GMT + 5:30)
        ist = gmt + td(hours=5, minutes=30)

        # Convert back to string format for output
        ist = ist.strftime('%I:%M %p') # you can change the format as per requirement

        return ist

    except:
        return "Invalid time format"