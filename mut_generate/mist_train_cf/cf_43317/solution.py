"""
QUESTION:
Write a function `extract_log_info` that takes a list of log messages as input and returns a list of tuples containing the extracted message and line number from each log message. The regular expression `r'^(?P<message>.+). Occurred at lines: (?P<line>\d+)'` should be used to match the pattern in the log messages. The function should use a while loop or an equivalent approach to iterate through the log messages and extract the required information, aiming to improve performance.
"""

import re

def extract_log_info(log_messages):
    regex = r'^(?P<message>.+). Occurred at lines: (?P<line>\d+)'
    extracted_info = []
    for message in log_messages:
        match = re.match(regex, message)
        if match:
            extracted_info.append((match.group('message'), match.group('line')))
    return extracted_info