"""
QUESTION:
Create a regular expression that matches valid IP addresses, which are composed of four numbers between 0 and 255 separated by dots, where each number does not have leading zeros unless the number is 0 itself. The function name should be `ip_address`.
"""

import re

def ip_address(ip):
    return bool(re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip))