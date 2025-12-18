"""
QUESTION:
Write a function named `convert_time` that takes a string representing time in 24-hour format "HH:MM" as input, and returns the time in 12-hour format "HH:MM AM/PM". The function should have a time complexity of O(1) and a space complexity of O(1). The function should correctly handle all possible inputs, including "12:00".
"""

def convert_time(time):
    hour = int(time[:2])
    minute = int(time[3:])

    if hour >= 12:
        suffix = "PM"
        if hour > 12:
            hour -= 12
    else:
        suffix = "AM"
        if hour == 0:
            hour = 12

    return str(hour) + ":" + str(minute).zfill(2) + " " + suffix