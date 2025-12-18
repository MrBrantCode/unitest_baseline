"""
QUESTION:
Write a function `calculate_login_duration` that takes two parameters: `log_in_time` and `log_out_time`, both in the format 'YYYY-MM-DD HH:MM:SS'. The function should return the number of minutes between `log_in_time` and `log_out_time`, handling cases where the times are in different months and years, and accounting for leap years and daylight saving time.
"""

from datetime import datetime

def calculate_login_duration(log_in_time, log_out_time):
    # Convert the input strings to datetime objects
    login = datetime.strptime(log_in_time, '%Y-%m-%d %H:%M:%S')
    logout = datetime.strptime(log_out_time, '%Y-%m-%d %H:%M:%S')

    # Calculate the time difference
    duration = logout - login

    # Convert the time difference to minutes
    minutes = duration.total_seconds() // 60

    return minutes