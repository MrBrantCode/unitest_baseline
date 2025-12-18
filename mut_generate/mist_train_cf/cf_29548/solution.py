"""
QUESTION:
Implement a function `calculate_progress_checks` that takes three parameters: `match_time` (integer) representing the total time duration of the match in milliseconds, `time_step` (integer) representing the time step in milliseconds used to advance the match time, and `progress_check_threshold` (float) representing the threshold value for progress check. The function should return the total number of progress checks made by the referee during the match, where the progress checks are made based on the match time, progress check steps, and progress check threshold.
"""

from math import ceil

def calculate_progress_checks(match_time, time_step, progress_check_threshold):
    progress_check_steps = ceil(15 / (time_step / 1000.0))  
    total_checks = match_time / time_step  
    checks_per_progress_check = ceil(total_checks / progress_check_steps)  
    progress_checks = ceil(total_checks / checks_per_progress_check)  
    return progress_checks