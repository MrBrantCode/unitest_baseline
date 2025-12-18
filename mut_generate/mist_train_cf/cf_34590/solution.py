"""
QUESTION:
Implement a function `convertSecondsToTime` that takes an integer `seconds` as input and returns a string representing the time in the format "hh:mm:ss". The input `seconds` is the total number of seconds and the output should represent this time in hours, minutes, and seconds.
"""

def convertSecondsToTime(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}:{minutes}:{seconds}"