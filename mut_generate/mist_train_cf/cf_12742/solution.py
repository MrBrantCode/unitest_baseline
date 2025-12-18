"""
QUESTION:
Write a function named `format_date_time` that takes two string parameters `date_str` and `time_str` representing a date in the format "YYYY-MM-DD" and a time in the format "HH:MM:SS", respectively. The function should return a string representing the input date and time in the format "Day, Month DD, YYYY HH:MM:SS AM/PM".
"""

import datetime

def format_date_time(date_str, time_str):
    """
    Format the input date and time string into a string representing the input date and time in the format "Day, Month DD, YYYY HH:MM:SS AM/PM".

    Args:
        date_str (str): A date string in the format "YYYY-MM-DD".
        time_str (str): A time string in the format "HH:MM:SS".

    Returns:
        str: A string representing the input date and time in the desired format.
    """
    # Convert input to datetime objects
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    time = datetime.datetime.strptime(time_str, "%H:%M:%S").time()

    # Format the date and time
    formatted_date = date.strftime("%A, %B %d, %Y")
    formatted_time = time.strftime("%I:%M:%S %p")

    # Return the formatted date and time
    return formatted_date + " " + formatted_time