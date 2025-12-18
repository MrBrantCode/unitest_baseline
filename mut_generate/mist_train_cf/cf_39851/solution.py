"""
QUESTION:
Write a function `extract_error_details` that takes a log message as input and extracts the file name, line number, and error message. The file name should be in the format `xxx.xxx`, the line number should be an integer, and the error message should be the remaining part of the log message after the file name and line number. The file name and line number are separated by a space and a colon, followed by another space and then the error message. The function should return `None` if the log message does not match the expected format.
"""

import re

def extract_error_details(log_message):
    pattern = r'(\w+\.\w+) (\d+):(\d+)\s+(.+)'
    match = re.search(pattern, log_message)
    if match:
        file_name = match.group(1)
        line_number = match.group(2)
        error_message = match.group(4)
        return file_name, int(line_number), error_message
    else:
        return None