"""
QUESTION:
Implement a Python class `IP` that takes an IP address string as input. The class should have methods to validate the IP address (IPv4 or IPv6), convert it to binary format, and calculate the network address and broadcast address given a subnet mask. The subnet mask should also be a string. Use the `ipaddress` module for IP address operations and validations. The class methods should be `__init__`, `validate_ip`, `to_binary`, and `calculate_network_broadcast`.
"""

import ipaddress

def entrance(address: str, subnet_mask: str = None) -> (bool, str, str, str):
    """
    Validates the IP address (IPv4 or IPv6), converts it to binary format, 
    and calculates the network address and broadcast address given a subnet mask.

    Args:
        address (str): The IP address string.
        subnet_mask (str, optional): The subnet mask string. Defaults to None.

    Returns:
        tuple: A tuple containing the validation result, binary IP address, 
        network address, and broadcast address.
    """
    try:
        ip_obj = ipaddress.ip_address(address)
        binary_ip = bin(int(ip_obj))[2:]
        
        if subnet_mask is None:
            return True, binary_ip, None, None
        
        network = ipaddress.ip_network(f"{address}/{subnet_mask}", strict=False)
        return True, binary_ip, str(network.network_address), str(network.broadcast_address)
    
    except ValueError:
        return False, None, None, None