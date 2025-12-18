"""
QUESTION:
Implement a function `is_ip_in_range(ip, start_ip, end_ip)` to check if a given IP address `ip` is within a certain range defined by `start_ip` and `end_ip`. The function should return `True` if `ip` is within the range (inclusive), and `False` otherwise. The function should have a time complexity of O(1).
"""

import ipaddress

def is_ip_in_range(ip, start_ip, end_ip):
    ip = ipaddress.ip_address(ip)
    start_ip = ipaddress.ip_address(start_ip)
    end_ip = ipaddress.ip_address(end_ip)
    return start_ip <= ip <= end_ip