"""
QUESTION:
Write a function `get_opening_hours(hours, day)` where hours is a tuple of 7 integers representing the opening hours of a business, with 0 indicating closed, 1 indicating open all day, and 2 indicating open for specific hours. The day parameter is an integer representing the day of the week (0 for Monday, 1 for Tuesday, and so on). The function should return a string representing the opening hours for the given day, in the format "Closed", "Open all day", or "Open from HH:MM to HH:MM".
"""

from typing import Tuple

def entrance(hours: Tuple[int, int, int, int, int, int, int], day: int) -> str:
    day_hours = hours[day]
    if day_hours == 0:
        return "Closed"
    elif day_hours == 1:
        return "Open all day"
    else:
        return "Open from 09:00 to 17:00"  # Replace with actual opening hours based on the day