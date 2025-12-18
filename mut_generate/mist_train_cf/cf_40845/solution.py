"""
QUESTION:
Implement a function `calculate_total_injuries` that calculates the total number of injuries in a sports team over a given period of time. The function takes in an array of integers representing the number of injuries each day and returns the total number of injuries. The number of injuries on a particular day is the sum of the injuries on that day and the injuries on the previous day, minus the number of injuries two days prior. If there are no injuries two days prior, the number of injuries on that day is simply the sum of the injuries on that day and the injuries on the previous day.
"""

from typing import List

def calculate_total_injuries(injuries: List[int]) -> int:
    total_injuries = 0
    prev_injuries = 0
    prev_prev_injuries = 0

    for current_injuries in injuries:
        total_injuries += current_injuries + prev_injuries - prev_prev_injuries
        prev_prev_injuries = prev_injuries
        prev_injuries = current_injuries

    return total_injuries