"""
QUESTION:
Implement a function `find_free_blocks` that takes a list of time slots as input, where each time slot is a tuple of two datetime objects representing the start and end times. The function should return a list of tuples representing the contiguous blocks of free time between the given time slots.

The input list of time slots is assumed to be sorted by the start time of each slot. The function should be efficient and handle overlapping time slots by merging them into a single block.

The output list of free time blocks should contain tuples with the start and end times of each free block.
"""

from typing import List, Tuple
from datetime import datetime

def find_free_blocks(time_slots: List[Tuple[datetime, datetime]]) -> List[Tuple[datetime, datetime]]:
    free_blocks = []
    if not time_slots:
        return free_blocks
    
    start_time = time_slots[0][0]
    end_time = time_slots[0][1]

    for slot in time_slots[1:]:
        if slot[0] > end_time:  
            free_blocks.append((end_time, slot[0]))
            start_time = slot[0]
            end_time = slot[1]
        else:
            end_time = max(end_time, slot[1])

    return free_blocks