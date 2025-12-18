"""
QUESTION:
Create a function `convert_to_12_hour_gmt5(time_str)` that takes a 24-hour time string in the format "HH:MM" as input and returns its equivalent 12-hour time string, considering the time zone GMT+5.
"""

def convert_to_12_hour_gmt5(time_str):
    hours, minutes = map(int, time_str.split(':'))
    gmt5_hours = (hours - 5) % 24
    am_pm = ' AM' if gmt5_hours < 12 else ' PM'
    gmt5_hours = gmt5_hours % 12 if gmt5_hours != 0 else 12
    return f'{gmt5_hours}:{minutes:02d}{am_pm}'