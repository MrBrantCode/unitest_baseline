"""
QUESTION:
Write a function named `in_time_period` that takes three parameters: `start_time` of type `datetime.time`, `end_time` of type `datetime.time`, and `current_time` of type `datetime.datetime`. The function should return `True` if the `current_time` falls within the time period from `start_time` to `end_time`, considering cases where the time period crosses midnight.
"""

from datetime import time

def in_time_period(start_time, end_time, current_time):
    if start_time < end_time:
        return start_time <= current_time.time() <= end_time
    else: # crosses midnight
        return start_time <= current_time.time() or current_time.time() <= end_time