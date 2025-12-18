"""
QUESTION:
Implement a function `process_data` that takes a list of data points in the format `(timestamp, frequency, value)` and returns a dictionary where the keys are the timestamps and the values are lists of tuples containing the corresponding frequency, value, and the time difference from the anchor timestamp (which is always 0). The function should group the data points based on their timestamps.
"""

from typing import List, Tuple, Dict

def process_data(data: List[Tuple[int, str, float]]) -> Dict[int, List[Tuple[str, float, int]]]:
    result_dict = {}
    for point in data:
        timestamp = point[0]
        if timestamp not in result_dict:
            result_dict[timestamp] = []
        result_dict[timestamp].append((point[1], point[2], 0))
    return result_dict