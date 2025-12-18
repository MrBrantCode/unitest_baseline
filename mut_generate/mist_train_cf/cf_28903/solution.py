"""
QUESTION:
Create a function `generate_event_count_matrix` that takes in two parameters: `raw_data` and `event_mapping_data`. The `raw_data` is a list of tuples containing a label and a time value, and `event_mapping_data` is a list of event indices corresponding to the logs in `raw_data`. The function should return a matrix `event_count_matrix` representing the count of events for each log sequence vector and a list `labels` where 1 represents an anomaly. The function should process the input data to generate the required outputs.

Restrictions: The function should be implemented using Python and should follow the given function signature: `def generate_event_count_matrix(raw_data: List[Tuple[str, int]], event_mapping_data: List[int]) -> Tuple[List[List[int]], List[int]]`.
"""

from typing import List, Tuple

def generate_event_count_matrix(raw_data: List[Tuple[str, int]], event_mapping_data: List[int]) -> Tuple[List[List[int]], List[int]]:
    event_count_matrix = []
    labels = []

    unique_events = list(set(event_mapping_data))
    unique_events.sort()

    for i in range(len(raw_data)):
        event_count = [0] * len(unique_events)
        event_index = unique_events.index(event_mapping_data[i])
        event_count[event_index] += 1
        event_count_matrix.append(event_count)

    for i in range(len(event_count_matrix)):
        if sum(event_count_matrix[i]) > 1:
            labels.append(1)
        else:
            labels.append(0)

    return event_count_matrix, labels