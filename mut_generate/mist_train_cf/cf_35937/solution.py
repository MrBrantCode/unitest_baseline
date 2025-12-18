"""
QUESTION:
Implement a function `validate_duration` that takes a duration string in the format "PnYnMnDTnHnMnS" and a list of allowed duration values as input. The function should return `True` if the input duration matches any of the allowed duration values and `False` otherwise. The function should also validate the format of the input duration string and return `False` for invalid formats.
"""

from typing import List
import re

def validate_duration(duration: str, allowed_durations: List[str]) -> bool:
    duration_pattern = re.compile(r'^P(\d+Y)?(\d+M)?(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?)?$')

    if not duration_pattern.match(duration):
        return False  # Invalid duration format

    return duration in allowed_durations