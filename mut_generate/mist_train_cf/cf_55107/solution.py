"""
QUESTION:
Calculate the time in a geographical area designated by UTC-5 given a time in Japan Standard Time (JST, UTC+9), taking into account the 14-hour difference between the two time zones. The function should also consider Daylight Saving Time (DST) if applicable. The function name is not specified, so name it as you like, for example, `convert_jst_to_utc_minus_five`.
"""

from datetime import datetime, timedelta

def convert_jst_to_utc_minus_five(jst_time):
    """
    This function converts a given time in Japan Standard Time (JST, UTC+9) to a time in a geographical area designated by UTC-5.
    
    Parameters:
    jst_time (datetime): Time in Japan Standard Time.
    
    Returns:
    datetime: Time in the geographical area designated by UTC-5.
    """
    # Calculate the 14-hour difference between JST and UTC-5
    utc_minus_five_time = jst_time - timedelta(hours=14)
    
    return utc_minus_five_time