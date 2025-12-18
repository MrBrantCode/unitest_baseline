"""
QUESTION:
Write a function `milliseconds_in_hours` that calculates the total number of milliseconds in a given number of hours. The function should take one argument `hours` and return the total number of milliseconds. Assume there are 60 seconds in a minute and 60 minutes in an hour, and 1000 milliseconds in a second.
"""

def milliseconds_in_hours(hours):
    """
    Calculate the total number of milliseconds in a given number of hours.
    
    Parameters:
    hours (int): The number of hours.
    
    Returns:
    int: The total number of milliseconds.
    """
    # One second is equal to 1000 milliseconds
    # One minute is equal to 60 seconds
    # One hour is equal to 60 minutes
    return hours * 60 * 60 * 1000