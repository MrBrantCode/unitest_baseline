"""
QUESTION:
Write a function called time_to_peak that calculates the time it takes for a projectile to reach the peak of its trajectory given the initial velocity and launch angle in degrees. The function should convert the angle from degrees to radians and use the acceleration due to gravity as 9.8 m/s^2. The function should return the calculated time in seconds.
"""

import math

def time_to_peak(velocity, angle):
    # Convert angle from degrees to radians
    angle = math.radians(angle)
    
    # Calculate time to reach peak
    t = velocity * math.sin(angle) / 9.8
    return t