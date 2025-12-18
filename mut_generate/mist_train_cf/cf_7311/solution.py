"""
QUESTION:
Create a function `convert_gmt_to_local` that takes a GMT time and a list of time zones as input, and returns the corresponding local times for each time zone, accounting for daylight saving time (DST) and multiple time zones. The function should handle DST changes correctly for different time zones, time zone offsets from GMT that are not whole hours, and dates within a reasonable range. The function should also provide an option for the desired output format for the local time and handle errors and invalid inputs gracefully.
"""

from datetime import datetime
import pytz

def convert_gmt_to_local(gmt_time, time_zones, output_format='%Y-%m-%d %H:%M:%S'):
    """
    Convert GMT time to local time for multiple time zones.

    Args:
        gmt_time (str): The GMT time in the format 'YYYY-MM-DD HH:MM:SS'.
        time_zones (list): A list of time zone names.
        output_format (str): The desired output format for the local time. Defaults to '%Y-%m-%d %H:%M:%S'.

    Returns:
        dict: A dictionary with time zones as keys and their corresponding local times as values.
    """

    # Parse the GMT time
    gmt_time = datetime.strptime(gmt_time, '%Y-%m-%d %H:%M:%S')
    gmt_time = pytz.utc.localize(gmt_time)

    # Initialize an empty dictionary to store the local times
    local_times = {}

    # Iterate over each time zone
    for tz in time_zones:
        try:
            # Get the time zone object
            tz_obj = pytz.timezone(tz)

            # Convert the GMT time to local time
            local_time = gmt_time.astimezone(tz_obj)

            # Format the local time according to the desired output format
            local_time = local_time.strftime(output_format)

            # Store the local time in the dictionary
            local_times[tz] = local_time

        except pytz.UnknownTimeZoneError:
            print(f"Error: Unknown time zone '{tz}'")

    return local_times