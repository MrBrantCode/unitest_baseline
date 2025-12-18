"""
QUESTION:
Write a function named `calculate_logged_in_minutes` that calculates the total number of minutes a user has been logged in, given their `log_in_time` and `log_out_time` in the format 'YYYY-MM-DD HH:MM:SS'. The function should handle cases where the user logs in and out on different months and years, during daylight saving time transitions, and on leap years.
"""

from datetime import datetime, timedelta

def calculate_logged_in_minutes(log_in_time, log_out_time):
    login = datetime.strptime(log_in_time, '%Y-%m-%d %H:%M:%S')
    logout = datetime.strptime(log_out_time, '%Y-%m-%d %H:%M:%S')

    if login.year != logout.year or login.month != logout.month:
        days = (logout - login).days
        minutes = 0
        for i in range(days + 1):
            current_day = login + timedelta(days=i)
            if i == 0 and login.day != logout.day:
                midnight = datetime(current_day.year, current_day.month, current_day.day, 23, 59, 59)
                minutes += (midnight - login).seconds // 60 + 1
            elif i == days and login.day != logout.day:
                midnight = datetime(current_day.year, current_day.month, current_day.day, 0, 0, 0)
                minutes += (logout - midnight).seconds // 60 + 1
            else:
                minutes += 1440
        return minutes

    minutes = (logout - login).seconds // 60
    if minutes < 0:
        midnight = datetime(login.year, login.month, login.day, 23, 59, 59)
        minutes = (midnight - login).seconds // 60 + (logout - midnight).seconds // 60
    return minutes