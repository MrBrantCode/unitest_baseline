"""
QUESTION:
Calculate the total distance between two vehicles after a certain time period. 

The function `calculate_distance` should take two speeds (in km/h) and a time period (in hours) as parameters. The function should return the total distance (in km) between the two vehicles after the given time period, assuming they move in opposite directions from the same starting point.
"""

def calculate_distance(speed1, speed2, time):
    """
    Calculate the total distance between two vehicles after a certain time period.

    Parameters:
    speed1 (float): The speed of the first vehicle in km/h.
    speed2 (float): The speed of the second vehicle in km/h.
    time (float): The time period in hours.

    Returns:
    float: The total distance between the two vehicles after the given time period.
    """
    return (speed1 + speed2) * time