"""
QUESTION:
Create a function `parse_log_message(log_message)` that takes a log message string in the format "email Sent!  smtp server: {smtp} port: {port}" and returns a tuple containing the SMTP server and port extracted from the log message.
"""

import re

def entance(log_message):
    match = re.search(r'smtp server: (\S+) port: (\d+)', log_message)
    if match:
        smtp_server = match.group(1)
        port = match.group(2)
        return (smtp_server, port)
    else:
        return None