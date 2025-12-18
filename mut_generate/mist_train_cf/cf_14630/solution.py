"""
QUESTION:
Create a function `get_day_name` that takes an integer `day_number` between 1 and 7 (inclusive) as input and returns the corresponding name of the day.
"""

def get_day_name(day_number):
    """
    Returns the name of the day corresponding to the given day number.

    Args:
        day_number (int): An integer between 1 and 7 (inclusive) representing the day of the week.

    Returns:
        str: The name of the day.
    """
    if day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
    elif day_number == 7:
        return "Sunday"
    else:
        return "Invalid input!"