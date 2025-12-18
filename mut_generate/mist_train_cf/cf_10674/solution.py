"""
QUESTION:
Write a function `calculate_minutes_logged_in` that takes two string arguments, `log_in_time` and `log_out_time`, representing the login and logout times in the format 'HH:MM:SS'. Calculate the total number of minutes a user has been logged in, considering cases where the user logs in and out on the same day or different days.
"""

from datetime import datetime, timedelta

def calculate_minutes_logged_in(log_in_time, log_out_time):
    # Convert log_in_time and log_out_time to datetime objects
    log_in = datetime.strptime(log_in_time, '%H:%M:%S')
    log_out = datetime.strptime(log_out_time, '%H:%M:%S')
    
    # Calculate the difference in time
    time_diff = log_out - log_in
    
    # Check if the user logged out on the same day
    if log_in.date() == log_out.date():
        minutes_logged_in = time_diff.total_seconds() // 60
    else:
        # Calculate the minutes for the first day
        midnight = datetime.strptime('00:00:00', '%H:%M:%S')
        minutes_day1 = (midnight - log_in).total_seconds() // 60
        
        # Calculate the minutes for the last day
        minutes_day2 = (log_out - midnight).total_seconds() // 60
        
        # Calculate the minutes for the days in between
        days_in_between = (log_out.date() - log_in.date() - timedelta(days=1)).days
        minutes_in_between = days_in_between * 24 * 60
        
        # Calculate the total minutes logged in
        minutes_logged_in = minutes_day1 + minutes_day2 + minutes_in_between
    
    return minutes_logged_in