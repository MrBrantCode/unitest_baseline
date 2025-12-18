"""
QUESTION:
Implement a function `validateTimestamp(timestamp)` that takes a string `timestamp` as input in the format "YYYY-MM-DD HH:MM:SS" and returns `True` if the timestamp is valid and `False` otherwise. A valid timestamp should have a year in four digits, a month in two digits (01-12), a day in two digits (01-31), an hour in two digits (00-23), minutes in two digits (00-59), and seconds in two digits (00-59).
"""

import re

def validateTimestamp(timestamp: str) -> bool:
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]) (0\d|1\d|2[0-3]):([0-5]\d):([0-5]\d)$'
    return bool(re.match(pattern, timestamp))