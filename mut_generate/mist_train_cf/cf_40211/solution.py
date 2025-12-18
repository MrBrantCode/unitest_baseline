"""
QUESTION:
Implement a function `calculate_clock_angle` that takes two integers `hour` and `minute` as input, representing time in 24-hour format. The function should return the smallest angle in degrees between the hour and minute hands of an analog clock. The function must handle all possible inputs from 00:00 to 23:59.
"""

def calculate_clock_angle(hour, minute):
    # Calculate the angles made by the hour and minute hands with respect to 12 o'clock
    hour_angle = (hour % 12 + minute / 60) * 30  # 30 degrees per hour, 0.5 degrees per minute
    minute_angle = minute * 6  # 6 degrees per minute

    # Calculate the absolute difference between the two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle between the two possible angles
    return min(angle, 360 - angle)