"""
QUESTION:
Write a function named time_difference that calculates the total difference in minutes between multiple time intervals. The input to the function is a string of time intervals in the format "HH:MM - HH:MM" separated by commas. The time intervals may refer to different days, so if the end time of an interval is earlier than its start time, it is assumed to be on the next day. The function should return the total difference in minutes.
"""

def time_difference(times):
    total_difference = 0
    for time in times.split(', '):
        start, end = time.split(' - ')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        start_minutes = start_h * 60 + start_m
        end_minutes = end_h * 60 + end_m
        if end_minutes < start_minutes:
            end_minutes += 1440
        total_difference += end_minutes - start_minutes
    return total_difference