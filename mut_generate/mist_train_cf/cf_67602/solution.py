"""
QUESTION:
Calculate the distance traveled by an object moving at a significant fraction of the speed of light over a given time period. The function should be named 'calculate_distance'. The object moves at 0.8 times the speed of light (approximately 240,000 km/s or 864,000,000 km/hr) and travels for a specified number of hours, which is given as an argument to the function.
"""

def calculate_distance(hours):
    """
    Calculate the distance traveled by an object moving at 0.8 times the speed of light.
    
    Parameters:
    hours (float): The number of hours the object travels.
    
    Returns:
    float: The distance traveled by the object in kilometers.
    """
    speed_of_light_km_per_hr = 864000000  # Speed of light in km/hr
    fraction_of_speed = 0.8  # The fraction of the speed of light the object is moving at
    return speed_of_light_km_per_hr * fraction_of_speed * hours