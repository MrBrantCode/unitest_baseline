"""
QUESTION:
Given a list of hexadecimal numbers representing time durations in minutes, write a function `calculate_total_time(hex_times)` that takes in this list and returns a tuple containing the total time duration in hours and minutes. The input list will always contain valid hexadecimal numbers representing time durations.
"""

from typing import List, Tuple

def entance(hex_times: List[str]) -> Tuple[int, int]:
    total_minutes = sum(int(hex_time, 16) for hex_time in hex_times)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes