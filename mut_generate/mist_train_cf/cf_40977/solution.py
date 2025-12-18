"""
QUESTION:
Implement a function `find_event_by_date(year, day_number)` that takes a year and a day number as input and returns the name of the event scheduled for that day in the format `DayX_YYYY`. The events are stored in a list `days` and are named in the format `DayX_YYYY`, where `X` is the day number and `YYYY` is the year. If no event is scheduled for the given day, the function should return "No event scheduled". Assume that the events are scheduled for consecutive days starting from day 1 and that the necessary attributes and methods have been implemented for the events.
"""

def find_event_by_date(year, day_number, days):
    """
    This function takes a year and a day number as input and returns the name of the event scheduled for that day.
    
    Parameters:
    year (int): The year of the event.
    day_number (int): The day number of the event.
    days (list): A list of event classes.
    
    Returns:
    str: The name of the event scheduled for the given day, or "No event scheduled" if no event is found.
    """
    event_name = f"Day{day_number}_{year}"
    if event_name in [cls.__name__ for cls in days]:
        return event_name
    else:
        return "No event scheduled"