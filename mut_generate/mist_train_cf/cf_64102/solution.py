"""
QUESTION:
Write a function `calculate_distance` that calculates the distance between two vehicles after 30 minutes, considering their average speeds and the possibility of each vehicle reversing direction once during the 30 minutes. The function should take four arguments: `speed1` and `speed2` representing the average speeds of the two vehicles, and `reverse_minute1` and `reverse_minute2` representing the minute intervals at which the vehicles may reverse direction (0 to 30). The function should return the absolute difference in distance traveled by the two vehicles after 30 minutes.
"""

def calculate_distance(speed1, speed2, reverse_minute1=30, reverse_minute2=30):
    """
    Calculates the distance between two vehicles after 30 minutes, considering their average speeds 
    and the possibility of each vehicle reversing direction once during the 30 minutes.

    Args:
        speed1 (float): The average speed of the first vehicle.
        speed2 (float): The average speed of the second vehicle.
        reverse_minute1 (int, optional): The minute interval at which the first vehicle may reverse direction. Defaults to 30.
        reverse_minute2 (int, optional): The minute interval at which the second vehicle may reverse direction. Defaults to 30.

    Returns:
        float: The absolute difference in distance traveled by the two vehicles after 30 minutes.
    """
    reverse_minute1 = min(reverse_minute1, 30)
    reverse_minute2 = min(reverse_minute2, 30)
    distance1 = speed1 * reverse_minute1 - speed1 * (30 - reverse_minute1)
    distance2 = speed2 * reverse_minute2 - speed2 * (30 - reverse_minute2)
    return abs(distance1 - distance2)