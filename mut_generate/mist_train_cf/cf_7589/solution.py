"""
QUESTION:
Calculate the total distance traveled by an object given its initial velocity, time interval, and changing acceleration. 

The initial velocity is 12.5 m/s, the acceleration changes every 0.5 seconds with values [2.3, 3.1, 4.2, 1.8] m/s^2 for each 0.5-second interval, and the time interval is 4.768 seconds, rounded to the nearest hundredth decimal place. The acceleration list should repeat for the entire time interval. Implement the function 'calculate_distance' that calculates the total distance traveled.
"""

def calculate_distance(u, accelerations, t):
    """
    Calculate the total distance traveled by an object given its initial velocity, 
    time interval, and changing acceleration.

    Args:
        u (float): Initial velocity in m/s
        accelerations (list): List of accelerations in m/s^2
        t (float): Time interval in seconds

    Returns:
        float: Total distance traveled in meters
    """
    total_distance = 0
    current_velocity = u
    time_interval = 0.5

    for _ in range(int(t // time_interval)):
        acceleration = accelerations[_ % len(accelerations)]
        distance = (current_velocity * time_interval) + (0.5 * acceleration * (time_interval ** 2))
        total_distance += distance
        current_velocity += acceleration * time_interval

    # Calculate the distance for the remaining time
    remaining_time = t % time_interval
    if remaining_time > 0:
        acceleration = accelerations[int((t // time_interval)) % len(accelerations)]
        distance = (current_velocity * remaining_time) + (0.5 * acceleration * (remaining_time ** 2))
        total_distance += distance

    return round(total_distance, 2)