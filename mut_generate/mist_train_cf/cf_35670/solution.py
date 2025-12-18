"""
QUESTION:
Write a function `parse_log_entry(log_entry: str) -> dict` that takes a string representing a single log entry and extracts the relevant information from it. The log entry is structured as follows: `<remote_host> - <user_name> [<timestamp>] "<request_method> <request_url> <request_protocol>" <response_status_code> <response_size>`. The function should return a dictionary containing the extracted information in the specified format, with any missing fields represented as `None`.
"""

import re

def parse_log_entry(log_entry: str) -> dict:
    pattern = r'^(?P<remote_host>\S+) - (?P<user_name>\S+) \[(?P<timestamp>.*?)\] "(?P<request_method>\S+) (?P<request_url>\S+) (?P<request_protocol>.*?)" (?P<response_status_code>\d+) (?P<response_size>\S+)$'
    match = re.match(pattern, log_entry)
    if match:
        return match.groupdict()
    else:
        return {
            "remote_host": None,
            "user_name": None,
            "timestamp": None,
            "request_method": None,
            "request_url": None,
            "request_protocol": None,
            "response_status_code": None,
            "response_size": None
        }