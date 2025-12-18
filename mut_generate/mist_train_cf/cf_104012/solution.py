"""
QUESTION:
Create a function called `block_ip_port_range` to block traffic from a certain IP address attempting to access a specific port range. The function should take two parameters: the IP address to block and the port range (start and end ports). The function should return a dictionary representing the firewall rule with keys 'Source IP', 'Destination Port', and 'Action'.
"""

def block_ip_port_range(ip_address, port_range):
    """
    Creates a firewall rule to block traffic from a certain IP address attempting to access a specific port range.

    Args:
        ip_address (str): The IP address to block.
        port_range (tuple): A tuple containing the start and end ports of the range.

    Returns:
        dict: A dictionary representing the firewall rule.
    """
    return {
        'Source IP': ip_address,
        'Destination Port': f"{port_range[0]}-{port_range[1]}",
        'Action': 'Block'
    }