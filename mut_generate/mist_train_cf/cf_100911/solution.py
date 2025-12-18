"""
QUESTION:
Create a function called `availableTime` that takes two integers `start` and `end` representing start and end times in 24-hour format as input. The function should return a string representing a valid time slot. If the input times are not within the valid range (0-23) or the start time is greater than the end time, return `NOT_SELECTED_TIME`. If the start and end times are the same, return `NO_DURATION`. If the start and end times are both 0 or both 0 and 23, return `ANY_TIME_POSSIBLE`. Otherwise, return the time slot in the format `hh:00 to hh:00`.
"""

def availableTime(start, end):
    # Check for invalid input
    if start < 0 or end > 23 or start > end:
        return "NOT_SELECTED_TIME"
    
    # Check for zero start and end time
    if start == 0 and end == 23:
        return "ANY_TIME_POSSIBLE"
    
    # Check for zero duration
    if start == end:
        return "NO_DURATION"
    
    # Valid time slot, return formatted string
    return "{}:00 to {}:00".format(start, end)