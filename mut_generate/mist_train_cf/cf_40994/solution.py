"""
QUESTION:
Create a function `max_simultaneous_trains` that takes in a list of train schedules, where each schedule is a tuple of two integers representing the start and end time of a train's journey in seconds. The function should return the maximum number of trains that can run simultaneously without conflicting schedules. The function should be able to handle any number of train schedules, and the start and end times can be any non-negative integer.
"""

from typing import List, Tuple

def max_simultaneous_trains(train_schedules: List[Tuple[int, int]]) -> int:
    events = []
    for start, end in train_schedules:
        events.append((start, 1))  # 1 represents the start of a train journey
        events.append((end, -1))   # -1 represents the end of a train journey

    events.sort()  # Sort the events based on time

    max_trains = 0
    current_trains = 0
    for _, event_type in events:
        current_trains += event_type
        max_trains = max(max_trains, current_trains)

    return max_trains