"""
QUESTION:
Given a faster jogger's speed of 10 km/h, and a slower jogger's speed 15% slower than the faster jogger, calculate the distance by which the faster jogger is ahead after 90 minutes. The joggers start from the same spot.
"""

def faster_jogger_lead_distance(faster_jogger_speed, slower_jogger_speed_percentage_decrease, time_minutes):
    """
    Calculate the distance by which the faster jogger is ahead of the slower jogger.

    Args:
    faster_jogger_speed (float): The speed of the faster jogger in km/h.
    slower_jogger_speed_percentage_decrease (float): The percentage decrease in speed of the slower jogger.
    time_minutes (float): The time in minutes.

    Returns:
    float: The distance by which the faster jogger is ahead.
    """
    time_hours = time_minutes / 60
    distance_difference_percentage = slower_jogger_speed_percentage_decrease / 100
    faster_jogger_distance = faster_jogger_speed * time_hours
    return faster_jogger_distance * distance_difference_percentage

# use it as follows:
faster_jogger_speed = 10
slower_jogger_speed_percentage_decrease = 15
time_minutes = 90
print(faster_jogger_lead_distance(faster_jogger_speed, slower_jogger_speed_percentage_decrease, time_minutes))