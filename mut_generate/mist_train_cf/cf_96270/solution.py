"""
QUESTION:
Implement a function named `is_ip_in_range(ip, start_ip, end_ip)` that checks if a given IP address `ip` is within the range defined by `start_ip` and `end_ip`. The function should return `True` if `ip` is within the range and `False` otherwise. The function must validate the input IP addresses. The input IP addresses are in the format of four numbers separated by dots, ranging from 0 to 255.
"""

import ipaddress

def is_ip_in_range(ip, start_ip, end_ip):
    """
    Checks if a given IP address is within the range defined by start_ip and end_ip.
    
    Args:
        ip (str): The IP address to check.
        start_ip (str): The start of the IP range.
        end_ip (str): The end of the IP range.
    
    Returns:
        bool: True if the IP is within the range, False otherwise.
    """

    ip_obj = ipaddress.ip_address(ip)
    start_ip_obj = ipaddress.ip_address(start_ip)
    end_ip_obj = ipaddress.ip_address(end_ip)

    return start_ip_obj <= ip_obj <= end_ip_obj