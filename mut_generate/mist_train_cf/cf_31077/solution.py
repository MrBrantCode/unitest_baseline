"""
QUESTION:
Implement a function `convertTime` that takes an integer `minutes` as input and returns a string representing the time in hours and minutes in the format "hh:mm". The function should handle both positive and negative input values, displaying negative time with a leading minus sign.
"""

def convertTime(minutes):
    hours = minutes // 60
    mins = minutes % 60
    if minutes < 0:
        return f"-{abs(hours):02d}:{abs(mins):02d}"
    else:
        return f"{hours:02d}:{mins:02d}"