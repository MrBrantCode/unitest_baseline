"""
QUESTION:
Design a function called `is_valid_protocol` that determines whether a given quantum cryptography protocol is valid. The protocol is considered valid if it has the following properties: the protocol name is not empty and contains only alphanumeric characters and underscores, the protocol type is either 'QKD' or 'quantum entanglement', and the protocol version is a positive integer.
"""

def is_valid_protocol(protocol):
    """
    This function checks if a given quantum cryptography protocol is valid.

    Args:
        protocol (dict): A dictionary containing the protocol name, type, and version.

    Returns:
        bool: True if the protocol is valid, False otherwise.
    """
    # Check if the protocol name is not empty and contains only alphanumeric characters and underscores
    if not protocol['name'] or not protocol['name'].isalnum() and '_' not in protocol['name']:
        return False
    
    # Check if the protocol type is either 'QKD' or 'quantum entanglement'
    if protocol['type'] not in ['QKD', 'quantum entanglement']:
        return False
    
    # Check if the protocol version is a positive integer
    if not isinstance(protocol['version'], int) or protocol['version'] <= 0:
        return False
    
    # If all checks pass, the protocol is valid
    return True