"""
QUESTION:
Create a function called `is_valid_ip` that takes a string as input and returns True if the string is a valid IP address (either IPv4 or IPv6 format) and False otherwise. The function should use regular expressions to match the IP address format. The input string should only contain the IP address, without any leading or trailing characters.
"""

import re

def is_valid_ip(ip):
    """
    Checks if a given string is a valid IP address (either IPv4 or IPv6 format).
    
    Args:
        ip (str): The IP address to check.
    
    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    
    # Define IPv4 pattern
    ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    
    # Define IPv6 pattern
    ipv6_pattern = r'^((?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}|(?:[A-Fa-f0-9]{1,4}:){1,7}:|(?:[A-Fa-f0-9]{1,4}:){1,6}:(?:[A-Fa-f0-9]{1,4}:)?|(?:(?:[A-Fa-f0-9]{1,4}:){1,5}|:):(?:[A-Fa-f0-9]{1,4}:){1,2}|(?:(?:[A-Fa-f0-9]{1,4}:){1,4}|:):(?:[A-Fa-f0-9]{1,4}:){1,3}|(?:(?:[A-Fa-f0-9]{1,4}:){1,3}|:):(?:[A-Fa-f0-9]{1,4}:){1,4}|(?:(?:[A-Fa-f0-9]{1,4}:){1,2}|:):(?:[A-Fa-f0-9]{1,4}:){1,5}|[A-Fa-f0-9]{1,4}:(?:(?::[A-Fa-f0-9]{1,4}){1,6}|:)|:(?:(?::[A-Fa-f0-9]{1,4}){1,7}|:)|fe80:(?::[A-Fa-f0-9]{1,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[A-Fa-f0-9]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$'
    
    # Check if the IP address matches either the IPv4 or IPv6 pattern
    if re.match(ipv4_pattern, ip):
        return True
    elif re.match(ipv6_pattern, ip):
        return True
    else:
        return False