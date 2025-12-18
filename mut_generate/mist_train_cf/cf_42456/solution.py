"""
QUESTION:
Create a function named `find_interfaces_with_protocol_down` that takes one parameter: `interface_status_data`, a dictionary representing the interface status data where the keys are interface names and the values are dictionaries containing various attributes. The function should return a list of interface names that are up but have their protocol status down.
"""

def find_interfaces_with_protocol_down(interface_status_data):
    return [interface for interface, status in interface_status_data.items() if status['status'] == 'up' and status['protocol'] == 'down']