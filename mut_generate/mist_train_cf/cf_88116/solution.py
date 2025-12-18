"""
QUESTION:
Write a function `parse_ip_address(ip_address)` that takes a string representing an IP address as input, splits it into its octets, converts each octet into its binary representation using bitwise operations, and returns the sum of all the binary values as an integer. The function should also include error handling to check for valid IP addresses and return an error message "Invalid IP address" if the input IP address is invalid. A valid IP address consists of exactly 4 octets, each ranging from 0 to 255.
"""

def parse_ip_address(ip_address):
    """
    This function takes a string representing an IP address as input, 
    splits it into its octets, converts each octet into its binary representation 
    using bitwise operations, and returns the sum of all the binary values as an integer.
    
    Args:
    ip_address (str): A string representing an IP address.
    
    Returns:
    int: The sum of all the binary values as an integer if the IP address is valid.
    str: "Invalid IP address" if the input IP address is invalid.
    """
    
    # Split the IP address into its octets
    octets = ip_address.split(".")
    
    # Check if the IP address has exactly 4 octets
    if len(octets) != 4:
        return "Invalid IP address"
    
    # Initialize the sum of binary values
    binary_sum = 0
    
    # Iterate over each octet
    for octet in octets:
        try:
            # Convert the octet to an integer
            octet_int = int(octet)
            
            # Check if the octet is within the valid range
            if octet_int < 0 or octet_int > 255:
                return "Invalid IP address"
            
            # Convert the octet to its binary representation
            binary = bin(octet_int)[2:].zfill(8)
            
            # Add the binary value to the sum
            binary_sum += int(binary, 2)
        except ValueError:
            # Return an error message if an invalid octet is encountered
            return "Invalid IP address"
    
    # Return the sum of binary values
    return binary_sum