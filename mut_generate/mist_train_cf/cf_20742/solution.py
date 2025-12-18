"""
QUESTION:
Implement a function `is_ip_in_range(ip, start_ip, end_ip)` that takes three string arguments representing IP addresses and returns a boolean indicating whether the given `ip` is within the range defined by `start_ip` and `end_ip`. The function should validate each IP address and return `True` if `start_ip` ≤ `ip` ≤ `end_ip`, and `False` otherwise.
"""

import ipaddress

def is_ip_in_range(ip, start_ip, end_ip):
    ip_obj = ipaddress.ip_address(ip)
    start_ip_obj = ipaddress.ip_address(start_ip)
    end_ip_obj = ipaddress.ip_address(end_ip)

    return start_ip_obj <= ip_obj <= end_ip_obj