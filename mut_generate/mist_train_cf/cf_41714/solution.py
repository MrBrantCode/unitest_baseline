"""
QUESTION:
Implement a function `parse_range` that takes a string representing a range in the format "[start..end]" where start and end are integers. The function should return a set of integers and their corresponding float representations within the specified range, inclusive of both start and end. The input string will always be in the correct format.
"""

def parse_range(range_str):
    start, end = map(int, range_str[1:-1].split('..'))
    return {start, end, float(start), float(end)} | set(range(start + 1, end)) | {float(i) for i in range(start + 1, end)}