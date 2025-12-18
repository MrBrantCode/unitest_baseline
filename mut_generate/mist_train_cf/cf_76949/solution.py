"""
QUESTION:
Write a function named `bus_separation_distance` that calculates the cumulative distance between two buses traveling in opposite directions. The eastbound bus moves at a speed of 50km/h, and the westbound bus moves at a speed of 60km/h. The function should take the time traveled as input and return the total distance the buses are separated by.
"""

def bus_separation_distance(time_traveled):
    """
    Calculate the cumulative distance between two buses traveling in opposite directions.

    Args:
    time_traveled (float): The time the buses have been traveling in hours.

    Returns:
    float: The total distance the buses are separated by in kilometers.
    """
    eastbound_speed = 50  # km/h
    westbound_speed = 60  # km/h

    eastbound_distance = eastbound_speed * time_traveled
    westbound_distance = westbound_speed * time_traveled

    return eastbound_distance + westbound_distance