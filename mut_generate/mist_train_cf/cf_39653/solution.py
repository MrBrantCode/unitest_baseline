"""
QUESTION:
Convert a given time in microseconds to a human-readable format. Implement a function `microsToTime` that takes an integer representing time in microseconds and returns a string representing the time in the format "hours:minutes:seconds:milliseconds". Assume the input time will not exceed 24 hours (86,400,000 microseconds).
"""

def microsToTime(microseconds):
    milliseconds = microseconds // 1000
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}"