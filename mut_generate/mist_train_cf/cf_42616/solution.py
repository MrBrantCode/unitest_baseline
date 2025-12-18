"""
QUESTION:
Implement a function `parse_command_line_arguments(args)` that takes a string of command-line arguments as input and returns a tuple of port number and IP address if the arguments are provided in the correct format. 

The correct format requires the presence of both `-p <port>` and `-a <address>`, where `<port>` is an integer between 1024 and 65535 inclusive, and `<address>` is a valid IPv4 address in the format "xxx.xxx.xxx.xxx". If the arguments are not provided or are invalid, the function should return an error message.
"""

import re

def parse_command_line_arguments(args):
    port_pattern = r'-p (\d{4,5})'
    address_pattern = r'-a (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    port_match = re.search(port_pattern, args)
    address_match = re.search(address_pattern, args)

    if port_match and address_match:
        port = int(port_match.group(1))
        address = address_match.group(1)
        if 1024 <= port <= 65535:
            return port, address
        else:
            return "Error: Port number must be in the range 1024 to 65535"
    else:
        return "Error: Invalid command-line arguments"