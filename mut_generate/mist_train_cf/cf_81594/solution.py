"""
QUESTION:
Create a function `valid_ips` that takes a list of strings as input and returns a list of valid IPv4 addresses. A valid IPv4 address consists of four numbers between 0 and 255, inclusive, separated by dots. The function should exclude any string that does not represent a valid IPv4 address.
"""

import ipaddress

def valid_ips(ip_list):
    def is_valid_ipv4(ip):
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

    return [i for i in ip_list if is_valid_ipv4(i)]