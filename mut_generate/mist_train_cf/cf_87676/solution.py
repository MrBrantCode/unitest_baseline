"""
QUESTION:
Write a function `convert_cdt_to_est` that takes an hour in Central Daylight Time (CDT) as input and returns the equivalent hour in Eastern Standard Time (EST) without using built-in date and time functions. The function should consider the 2-hour difference between CDT and EST during daylight saving time transition, and adjust the result if it exceeds 23 hours.
"""

def convert_cdt_to_est(cdt_time):
    """
    Converts the given hour in Central Daylight Time (CDT) to Eastern Standard Time (EST).
    
    Args:
    cdt_time (int): The hour in CDT (0-23).
    
    Returns:
    int: The equivalent hour in EST.
    """
    est_time = (cdt_time + 2) % 24
    return est_time