"""
QUESTION:
Write a function `time_difference(times)` that takes a string of time intervals separated by commas, where each interval is in the format "HH:MM - HH:MM" and may span across different days. The function should return the total difference between all intervals in minutes.
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