"""
QUESTION:
Write a function called `london_to_nz` that converts 6:00 am London Time to New Zealand Standard Time, taking into account daylight saving time in both countries. The function should return the time in New Zealand as a string in the format "HH:mm" and consider both countries' standard and daylight saving times, but not public holidays. Assume the London time is in the format "HH:mm" and the year is provided.
"""

from datetime import datetime, timedelta

def london_to_nz(london_time: str, year: int) -> str:
    """
    Converts 6:00 am London Time to New Zealand Standard Time, 
    taking into account daylight saving time in both countries.

    Args:
    london_time (str): London Time in the format "HH:mm"
    year (int): The year of the London Time

    Returns:
    str: The time in New Zealand as a string in the format "HH:mm"
    """

    # Parse the input time and create a datetime object
    london_time = datetime.strptime(london_time, "%H:%M")

    # Create a datetime object for the start and end of daylight saving time in London and New Zealand
    london_dst_start = datetime(year, 3, 31, 1, 0, 0)
    london_dst_end = datetime(year, 10, 31, 1, 0, 0)
    nz_dst_start = datetime(year, 9, 30, 2, 0, 0)
    nz_dst_end = datetime(year, 4, 2, 2, 0, 0)

    # Check if it's daylight saving time in London and New Zealand
    is_london_dst = london_time.replace(year=london_dst_start.year) > london_dst_start and london_time.replace(year=london_dst_end.year) < london_dst_end
    is_nz_dst = london_time.replace(year=nz_dst_start.year) > nz_dst_start and london_time.replace(year=nz_dst_end.year) < nz_dst_end

    # Calculate the offset from London Time to New Zealand Time
    offset = 12
    if is_london_dst and not is_nz_dst:
        offset = 11
    elif not is_london_dst and is_nz_dst:
        offset = 13
    elif is_london_dst and is_nz_dst:
        offset = 12

    # Calculate the New Zealand Time
    nz_time = london_time + timedelta(hours=offset)

    # Format the New Zealand Time
    nz_time = nz_time.strftime("%H:%M")

    return nz_time