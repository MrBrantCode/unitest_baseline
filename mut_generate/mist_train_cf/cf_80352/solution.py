"""
QUESTION:
Create a function `distance_normalize` that takes an integer `distance_week` representing the total distance an employee travels in a week and returns the normalized distance score. Assume the standard work commute is 20 miles per day and a 5-day workweek. The normalized score is calculated by dividing the `distance_week` by the standard commute per week.
"""

def distance_normalize(distance_week):
    """
    Calculate the normalized distance score by dividing the total weekly distance
    by the standard weekly commute (20 miles/day * 5 days/week).

    Args:
        distance_week (int): Total distance an employee travels in a week.

    Returns:
        float: Normalized distance score.
    """
    std_commute_per_week = 20*5  # 20 miles/day * 5 days/week
    return distance_week / std_commute_per_week