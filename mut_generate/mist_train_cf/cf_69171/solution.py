"""
QUESTION:
Create a function named `process_ip` that takes a list of strings representing IP addresses as input. The function should return a list of strings where each string is the corresponding IP address with all periods removed if the IP address is valid, or an error message 'Error: Incorrect IP Address format' if the IP address is invalid. A valid IP address consists of four numbers separated by periods, where each number is between 0 and 255 and does not have leading zeros.
"""

import re

def process_ip(ip_list):
    results = []
    ip_pattern = re.compile(r"^(?:(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    
    for ip in ip_list:
        if ip_pattern.match(ip):
            results.append(ip.replace('.', ''))
        else:
            results.append('Error: Incorrect IP Address format')
    return results