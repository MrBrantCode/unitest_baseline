"""
QUESTION:
Implement a function `parse_listen_addr` that takes a string in the format `<ip_address>:<port>` as input, where `<ip_address>` can be either an IPv4 or IPv6 address, and `<port>` is a port number. The function should return a string in the format `'tcp:<port>:interface=<ip_address>'`, with IPv6 addresses enclosed in square brackets. If the input string does not match the expected format, the function should return an error message.
"""

import re

def parse_listen_addr(listen_addr):
    ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(\[?[0-9a-fA-F:]+\]?)'
    port_pattern = r'(\d{1,5})'
    pattern = re.compile(f'({ip_pattern}):({port_pattern})')

    match = pattern.match(listen_addr)
    if match:
        ip = match.group(1) if match.group(1) else match.group(2)
        port = match.group(3)
        if ':' in ip:  # IPv6 address
            return f'tcp:{port}:interface=[{ip}]'
        else:  # IPv4 address
            return f'tcp:{port}:interface={ip}'
    else:
        return 'Invalid listen address format'