"""
QUESTION:
Create a function `get_interface_name(ip_address: str, command_output: str) -> str` that takes an IP address and the output of the `ip address` command as input and returns the corresponding interface name. The function should parse the command output to build a dictionary mapping IP addresses to interface names. The command output format is shown above, with each interface described over multiple lines, and the IP address specified on the line starting with 'inet'. If the IP address is not found in the command output, return "Interface not found".
"""

import re

def get_interface_name(ip_address: str, command_output: str) -> str:
    ip_to_name = {}
    lines = command_output.split('\n')
    interface_name = ""
    found = False
    for line in lines:
        if line.startswith('inet ' + ip_address):
            found = True
        if found:
            interface_match = re.search(r'^\d+: (\w+):', line)
            if interface_match:
                interface_name = interface_match.group(1)
                break
    return interface_name if found else "Interface not found"