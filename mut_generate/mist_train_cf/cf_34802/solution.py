"""
QUESTION:
Implement the function `list_checked(calendars, request)` that takes in a list of calendars and a request for events. Each calendar is a list of tuples containing the event name and start time. The request is a tuple containing the event name and a start time range. Return a list of events that match the request and are present in the calendars. The function should have the following signature: `def list_checked(calendars: List[List[Tuple[str, int]]], request: Tuple[str, Tuple[int, int]]) -> List[Tuple[str, int]]`.
"""

from typing import List, Tuple

def list_checked(calendars: List[List[Tuple[str, int]]], request: Tuple[str, Tuple[int, int]]) -> List[Tuple[str, int]]:
    event_name, time_range = request
    start_time, end_time = time_range
    return [(event[0], event[1]) for calendar in calendars for event in calendar if event[0] == event_name and start_time <= event[1] <= end_time]