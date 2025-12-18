"""
QUESTION:
Write a function `extractLogInfo(log)` that takes a log message in the format `[timestamp] [log level] [message]` as input and returns the `timestamp` and `log level` as a tuple. The timestamp and log level are separated by a space, and the log level is a single word that does not contain any spaces. If the input log message does not match the expected format, the function should return `None`.
"""

import re

def extract_log_info(log):
    pattern = r'\[(.*?)\] (\w+) (.*)'
    match = re.match(pattern, log)
    if match:
        timestamp = match.group(1)
        log_level = match.group(2)
        return (timestamp, log_level)
    else:
        return None