"""
QUESTION:
Create a function `convert_to_hours` that takes time in milliseconds as input and returns the equivalent time in hours. The function should not take any additional parameters other than the milliseconds.
"""

def convert_to_hours(milliseconds):
    """
    Converts time in milliseconds to hours.
    
    Parameters:
    milliseconds (int): Time in milliseconds
    
    Returns:
    float: Equivalent time in hours
    """
    milliseconds_per_second = 1000
    seconds_per_hour = 3600
    return (milliseconds / (milliseconds_per_second * seconds_per_hour))