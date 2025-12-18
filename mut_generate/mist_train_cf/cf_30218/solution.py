"""
QUESTION:
Implement a function `get_time_members(data)` that takes a timestamp string in the format "YYYY-MM-DD HH:MM:SS" as input and returns a tuple containing the year, month, day, and hour as integers. Implement another function `process_file_data(file_data)` that takes a list of timestamps as input and returns a list of lists, where each sublist contains the year, month, and day extracted from the corresponding timestamp. The hour component is not required in the output. The output should be in the format: [[year, month, day], ...].
"""

from typing import List, Tuple

def entrance(timestamp: str) -> List[List[int]]:
    def get_time_members(timestamp: str) -> Tuple[int, int, int, int]:
        year, month, day = map(int, timestamp.split()[0].split('-'))
        hour = int(timestamp.split()[1].split(':')[0])
        return year, month, day, hour

    def process_file_data(file_data: List[str]) -> List[List[int]]:
        lines = []
        for data in file_data:
            year, month, day, _ = get_time_members(data)
            lines.append([year, month, day])
        return lines

    file_data = [timestamp]
    return process_file_data(file_data)