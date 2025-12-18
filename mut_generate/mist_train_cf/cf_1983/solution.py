"""
QUESTION:
Implement a function `calculate_total_work_hours` that takes a list of work sessions as input, where each session is a dictionary containing the start and end time of the session as strings in 'HH:MM' format. The function should calculate and return the total work hours by converting the start and end time strings to datetime objects and summing up the duration between them.
"""

from datetime import datetime

def calculate_total_work_hours(work_sessions):
    total_hours = 0
    for session in work_sessions:
        start_time = datetime.strptime(session['start_time'], '%H:%M')
        end_time = datetime.strptime(session['end_time'], '%H:%M')
        total_hours += (end_time - start_time).total_seconds() / 3600
    return total_hours