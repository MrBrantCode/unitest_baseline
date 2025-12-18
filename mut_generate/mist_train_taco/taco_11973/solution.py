"""
QUESTION:
Complete the function so that it returns the number of seconds that have elapsed between the start and end times given.  

##### Tips:
- The start/end times are given as Date (JS/CoffeeScript), DateTime (C#), Time (Nim), datetime(Python) and Time (Ruby) instances.  
- The start time will always be before the end time.
"""

def calculate_elapsed_seconds(start, end):
    """
    Calculate the number of seconds that have elapsed between the start and end times.

    Parameters:
    start (datetime): The start time.
    end (datetime): The end time.

    Returns:
    float: The number of seconds that have elapsed between the start and end times.
    """
    return (end - start).total_seconds()