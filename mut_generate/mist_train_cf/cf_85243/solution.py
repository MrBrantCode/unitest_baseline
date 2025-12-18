"""
QUESTION:
Calculate the distance traveled by an object moving at 0.8 times the speed of light for 4 hours. The speed of light is approximately 299,792 kilometers per second. Assume 1 hour is equal to 3,600 seconds. Implement a function named `space_distance` to calculate and return the distance traveled in kilometers.
"""

def space_distance(fraction_of_light_speed, hours):
    """
    Calculate the distance traveled by an object moving at a fraction of the speed of light for a given number of hours.
    
    Args:
        fraction_of_light_speed (float): The fraction of the speed of light.
        hours (int): The number of hours the object is moving.
    
    Returns:
        float: The distance traveled in kilometers.
    """
    
    speed_of_light = 299792  # km/s
    seconds_per_hour = 3600
    
    # Calculate the speed of the object
    object_speed = fraction_of_light_speed * speed_of_light
    
    # Calculate the total time in seconds
    total_seconds = hours * seconds_per_hour
    
    # Calculate the distance traveled
    distance = object_speed * total_seconds
    
    return distance