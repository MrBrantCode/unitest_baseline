"""
QUESTION:
Create a function `findClockAngle` that calculates the smaller angle (in degrees) between the hour and minute hands of a clock, given two integers `hour` and `minutes` as input. The `hour` input should be within the range of `1 <= hour <= 12` and the `minutes` input should be within the range of `0 <= minutes <= 59`. The solution should be accurate to within 10^-5 of the actual value.
"""

def findClockAngle(hour, minutes):
    # If the hour is 12 then set it to 0
    if hour == 12:
        hour = 0
    if minutes == 60:
        minutes = 0
        hour += 1
    # Calculate the angles moved by hour and minute hands with reference to 12:00
    hour_angle = 0.5 * (hour * 60 + minutes)
    minute_angle = 6 * minutes
    # Find the difference of two angles
    angle = abs(hour_angle - minute_angle)
    # Return the smaller angle of two possible angles
    angle = min(360 - angle, angle)
    return angle