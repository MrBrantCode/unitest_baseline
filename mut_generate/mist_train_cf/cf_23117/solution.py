"""
QUESTION:
Write a function `ipv4_to_binary(ip: str) -> str` that takes an input string representing an IPv4 address and returns its binary representation. The input string should first be validated to ensure it is a valid IPv4 address. A valid IPv4 address consists of exactly four parts separated by dots, each part consisting of digits only and having a value between 0 and 255 (inclusive). If the input string is not a valid IPv4 address, the function should return an error message.
"""

def ipv4_to_binary(ip: str) -> str:
    """
    This function takes an input string representing an IPv4 address, 
    validates it, and returns its binary representation.
    
    Args:
        ip (str): The input string representing an IPv4 address.
    
    Returns:
        str: The binary representation of the input IPv4 address if it's valid, 
             otherwise an error message.
    """
    # Validate the input IP address
    parts = ip.split('.')
    if len(parts) != 4:
        return f"{ip} is not a valid IPv4 address."
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return f"{ip} is not a valid IPv4 address."

    # Convert the IP address into its binary representation
    binary_parts = []
    for part in parts:
        binary_parts.append(format(int(part), '08b'))
    return '.'.join(binary_parts)