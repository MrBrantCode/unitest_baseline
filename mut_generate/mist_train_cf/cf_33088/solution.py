"""
QUESTION:
Create a function `calculate_duration` that takes two string parameters `start_time` and `end_time` in the format "HH:MM" (24-hour format), representing the start and end times respectively, where `start_time` will always be before `end_time`. The function should return a dictionary with keys "hours" and "minutes" representing the duration between the two times.
"""

def calculate_duration(start_time, end_time):
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))

    total_start_minutes = start_hour * 60 + start_minute
    total_end_minutes = end_hour * 60 + end_minute

    duration_minutes = total_end_minutes - total_start_minutes
    duration_hours = duration_minutes // 60
    remaining_minutes = duration_minutes % 60

    return {"hours": duration_hours, "minutes": remaining_minutes}