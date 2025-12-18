"""
QUESTION:
Write a function `find_conflicts` that takes a list of train schedules as input. The schedule is a list of tuples containing the station name, departure time, and arrival time. The function should return a list of tuples, where each tuple contains the names of the stations involved in a conflict and the conflicting times. A conflict occurs when the arrival time at a station is earlier than the departure time from the same station. 

The input schedule is represented as `List[Tuple[str, str, str]]` and the output should be `List[Tuple[str, str, str, str]]`. Time is represented in the format "HH:MM".
"""

from typing import List, Tuple
from datetime import datetime

def find_conflicts(schedule: List[Tuple[str, str, str]]) -> List[Tuple[str, str, str, str]]:
    conflicts = []
    for i in range(len(schedule) - 1):
        current_station, current_departure, current_arrival = schedule[i]
        next_station, next_departure, next_arrival = schedule[i + 1]
        
        current_departure_time = datetime.strptime(current_departure, "%H:%M")
        current_arrival_time = datetime.strptime(current_arrival, "%H:%M")
        next_departure_time = datetime.strptime(next_departure, "%H:%M")
        next_arrival_time = datetime.strptime(next_arrival, "%H:%M")
        
        if current_arrival_time > next_departure_time:
            conflicts.append((current_station, next_station, current_arrival, next_departure))
    
    return conflicts