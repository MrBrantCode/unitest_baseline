"""
QUESTION:
Write a function named `biker_average_speed` to calculate the actual average speed of a biker on a round trip. The function should take as input the distances traveled downhill, uphill, and on flat road, as well as the speeds at which the biker travels in each terrain, and the fixed percentage that the wind speed affects the biker's speed.
"""

def biker_average_speed(distance_downhill, speed_downhill, distance_uphill, speed_uphill, distance_flat, speed_flat, wind_percentage):
    """
    Calculate the actual average speed of a biker on a round trip.

    Args:
        distance_downhill (float): Distance traveled downhill.
        speed_downhill (float): Speed while traveling downhill.
        distance_uphill (float): Distance traveled uphill.
        speed_uphill (float): Speed while traveling uphill.
        distance_flat (float): Distance traveled on flat road.
        speed_flat (float): Speed while traveling on flat road.
        wind_percentage (float): Fixed percentage that the wind speed affects the biker's speed.

    Returns:
        float: The actual average speed of the biker on the round trip.
    """

    # Calculate the total distance traveled
    total_distance = distance_downhill + distance_uphill + distance_flat

    # Calculate the time taken for each segment of the trip
    time_downhill = distance_downhill / (speed_downhill * (1 + wind_percentage / 100))
    time_uphill = distance_uphill / (speed_uphill * (1 - wind_percentage / 100))
    time_flat = distance_flat / (speed_flat * (1 - wind_percentage / 100))

    # Calculate the total time taken for the round trip
    total_time = time_downhill + time_uphill + time_flat

    # Calculate the actual average speed
    average_speed = total_distance / total_time

    return average_speed