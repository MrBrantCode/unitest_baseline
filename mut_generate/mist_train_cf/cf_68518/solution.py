"""
QUESTION:
Create a function called `max_height_times` that accepts an array of positive integer velocities and calculates the time 't' at which each ball reaches its maximum height using the formula h = -16t^2 + vt + 10. The function should also determine which ball reaches the maximum height and at what time.
"""

def max_height_times(velocities):
    max_times = []
    for v in velocities:
        max_time = float(v) / (2 * 16)   
        max_times.append(max_time)
  
    max_velocity = max(velocities)  
    max_time_velocity = float(max_velocity) / (2 * 16) 
  
    return max_times, max_velocity, max_time_velocity