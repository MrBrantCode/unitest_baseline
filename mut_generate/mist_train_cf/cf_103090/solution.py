"""
QUESTION:
Create a function called `miles_to_km` that takes two parameters: a distance in miles and the time it takes to travel that distance in minutes. The function should return two values: the distance in kilometers and the speed in kilometers per hour.
"""

def miles_to_km(miles, time):
    """
    Convert a distance in miles to kilometers and calculate the speed in kilometers per hour.

    Args:
        miles (float): Distance in miles.
        time (float): Time in minutes.

    Returns:
        tuple: A tuple containing the distance in kilometers and the speed in kilometers per hour.
    """
    # Convert miles to kilometers
    kilometers = miles * 1.60934
    
    # Calculate speed in kilometers per hour
    speed = kilometers / (time / 60)   # Assuming time is given in minutes
    
    return kilometers, speed