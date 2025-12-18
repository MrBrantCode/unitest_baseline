"""
QUESTION:
Implement the function `calculate_total_duration(durations)` that takes a list of time duration strings in the format "HH:MM:SS" as input and returns the total duration in seconds. The function should skip any invalid time duration strings that contain non-numeric characters or do not match the "HH:MM:SS" format.
"""

from typing import List

def entance(durations: List[str]) -> int:
    total_seconds = 0
    for duration in durations:
        try:
            hours, minutes, seconds = map(int, duration.split(':'))
            if hours >= 0 and minutes >= 0 and seconds >= 0 and hours < 24 and minutes < 60 and seconds < 60:
                total_seconds += hours * 3600 + minutes * 60 + seconds
        except (ValueError, IndexError):
            continue
    return total_seconds