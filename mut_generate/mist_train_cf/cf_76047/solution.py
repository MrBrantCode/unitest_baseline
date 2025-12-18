"""
QUESTION:
Write a function `projectile_motion(initial_velocity, launch_angle)` that calculates and returns the time of flight, maximum height, and total distance travelled by an object launched from the ground at the given initial velocity and launch angle, considering the acceleration due to gravity to be 9.8 m/s² and assuming no air resistance. The initial velocity and launch angle should be input parameters in units of meters per second (m/s) and degrees, respectively.
"""

import math

def projectile_motion(initial_velocity, launch_angle):
    # Converting the angle to radians
    launch_angle_rad = math.radians(launch_angle)
    
    # Calculating time of flight
    g = 9.8  # acceleration due to gravity
    time_of_flight = 2*initial_velocity*math.sin(launch_angle_rad) / g
    
    # Calculating maximum height
    max_height = (initial_velocity**2)*(math.sin(launch_angle_rad)**2) / (2*g)
    
    # Calculating range
    total_distance = (initial_velocity**2)*math.sin(2*launch_angle_rad) / g
    
    return time_of_flight, max_height, total_distance