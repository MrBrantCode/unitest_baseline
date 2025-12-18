"""
QUESTION:
Write a function `calculate_age` that calculates the age of a person given their birth year and the year an event occurred. The function should take two parameters, `birth_year` and `event_year`, and return the age of the person during the event.
"""

def calculate_age(birth_year, event_year):
    """
    Calculate the age of a person given their birth year and the year an event occurred.

    Parameters:
    birth_year (int): The year the person was born
    event_year (int): The year the event occurred

    Returns:
    int: The age of the person during the event
    """
    return event_year - birth_year