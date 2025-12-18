"""
QUESTION:
Write a function `get_duration(times)` that takes a list of two valid times in 24-hour format ("HH:MM:SS") and returns the duration in seconds between them. The function should assume the input list always contains two valid times and the duration does not exceed 86400 seconds (24 hours). The time complexity of the solution should be O(1).
"""

def get_duration(times):
    time1 = times[0].split(":")
    time2 = times[1].split(":")
    
    hours1, minutes1, seconds1 = int(time1[0]), int(time1[1]), int(time1[2])
    hours2, minutes2, seconds2 = int(time2[0]), int(time2[1]), int(time2[2])
    
    duration1 = hours1 * 3600 + minutes1 * 60 + seconds1
    duration2 = hours2 * 3600 + minutes2 * 60 + seconds2
    
    difference = duration2 - duration1
    
    if difference < 0:
        difference += 86400
    
    return difference