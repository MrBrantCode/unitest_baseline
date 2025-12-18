"""
QUESTION:
Write a function `convert_mst_to_ast` that takes a string representing a date and time in Mountain Standard Time (MST) in the format "YYYY-MM-DD 23:45" and returns the equivalent date and time in Atlantic Standard Time (AST) as a string in the same format. Assume that the input string is a valid date and time in MST.
"""

from datetime import datetime
from pytz import timezone

def convert_mst_to_ast(mst_time_str):
    # Define datetime format
    datetime_format = "%Y-%m-%d %H:%M"

    # Define time zones
    mst_tz = timezone('MST')
    ast_tz = timezone('Canada/Atlantic')  

    # Parse string to datetime object
    mst_time = datetime.strptime(mst_time_str, datetime_format)

    # Set the timezone for the datetime object
    mst_time = mst_tz.localize(mst_time)

    # Convert to AST timezone
    ast_time = mst_time.astimezone(ast_tz)

    # Convert datetime object to string
    ast_time_str = ast_time.strftime(datetime_format)

    return ast_time_str